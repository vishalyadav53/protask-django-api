from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Task

class TaskAPITestCase(APITestCase):

    def setUp(self):
        # 1. Test ke liye ek fresh user banaya
        self.user = User.objects.create_user(username='testuser', password='testpassword123')
        self.url = reverse('task-list')  # Hamara /api/tasks/ endpoint
        
        # Registration URL nikalne ke liye rasta set kiya
        self.register_url = reverse('auth_register')  # Hamara /auth/register/ endpoint

        # 2. Script ke liye JWT Access Token generate kiya
        refresh = RefreshToken.for_user(self.user)
        self.access_token = str(refresh.access_token)

    def test_create_task_authenticated(self):
        # Test 1: Sahi Token ke sath task banana
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        data = {"title": "Mera Ek Dam Sahi Long Title", "description": "Automated testing", "is_completed": False}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_task_unauthenticated(self):
        # Test 2: Bina token ke task banana (401 Error)
        self.client.credentials()
        data = {"title": "Mera Unauthorized Long Title", "description": "Bina token"}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_search_and_pagination(self):
        # Test 3: Search aur Pagination check karna
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        Task.objects.create(user=self.user, title="Mera Pehla Secured Task", description="Test 1")
        Task.objects.create(user=self.user, title="Normal Django Task", description="Test 2")
        
        search_url = f"{self.url}?search=Secured"
        response = self.client.get(search_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)

    # 👇 YEH HAI NAYA TEST CASE (Registration test karne ke liye)
    def test_user_registration(self):
        # Test 4: Ek naye normal user ko register karke dekhna
        registration_data = {
            "username": "newnormaluser",
            "password": "newpassword123",
            "email": "normaluser@example.com"
        }
        # Hum bina kisi token ke POST request bhejenge kyunki registration open hota hai
        response = self.client.post(self.register_url, registration_data, format='json')
        
        # Check 1: Kya status code 201 Created aaya?
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        # Check 2: Kya database me sach me ek naya user jud gaya?
        self.assertTrue(User.objects.filter(username="newnormaluser").exists())