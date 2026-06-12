from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, UserRegisterView

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('', include(router.urls)), 
    # 👇 Iska rasta humne 'api/register/' kar diya taaki yeh alag se sabse upar dikhe
    path('register/', UserRegisterView.as_view(), name='auth_register'),  
]