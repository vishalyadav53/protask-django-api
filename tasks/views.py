from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import get_user_model
from .models import Project, Task
from .serializers import UserSerializer, ProjectSerializer, TaskSerializer
# Create your views here.

User = get_user_model()

# 1. USER REGISTRATION VIEW
class UserRegistrationViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]  # Anyone can sign up


# 2. PROJECT VIEWSET (Handles CRUD for Projects)
class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]  # Must be logged in to access

    def get_queryset(self):
        # N+1 Optimization: prefetch_related caches nested tasks data instantly
        return Project.objects.prefetch_related('tasks').all()

    def perform_create(self, serializer):
        # Automatically set the 'created_by' field to the logged-in user
        serializer.save(created_by=self.request.user)


# 3. TASK VIEWSET (Handles CRUD for Tasks)
class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # N+1 Optimization: select_related joins User table to fetch details efficiently
        queryset = Task.objects.select_related('project').prefetch_related('assigned_to').all()
        
        # Adding Basic Search/Filter functionality via URL parameters
        status_param = self.request.query_params.get('status')
        if status_param:
            queryset = queryset.filter(status=status_param)
        return queryset
