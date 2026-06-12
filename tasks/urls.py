from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserRegistrationViewSet, ProjectViewSet, TaskViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'register', UserRegistrationViewSet, basename='user-register')
router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'tasks', TaskViewSet, basename='task')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]