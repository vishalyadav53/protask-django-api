from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Project, Task

User = get_user_model()

# 1. USER SERIALIZER (For Registration & Profile details)
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role', 'password']
        extra_kwargs = {'password': {'write_only': True}}  # Security measure

    def create(self, validated_data):
        # Securely hash the password before saving to the database
        user = User.objects.create_user(**validated_data)
        return user


# 2. TASK SERIALIZER
class TaskSerializer(serializers.ModelSerializer):
    # This displays the email of assigned users instead of just their ID numbers
    assigned_to_details = UserSerializer(source='assigned_to', many=True, read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'project', 'title', 'status', 'priority', 'assigned_to', 'assigned_to_details', 'due_date']


# 3. PROJECT SERIALIZER
class ProjectSerializer(serializers.ModelSerializer):
    # Nested Serializer: Automatically lists all tasks belonging to this project
    tasks = TaskSerializer(many=True, read_only=True)
    created_by_email = serializers.CharField(source='created_by.email', read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'created_by_email', 'created_at', 'tasks']