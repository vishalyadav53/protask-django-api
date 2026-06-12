from rest_framework import serializers
from django.contrib.auth.models import User  # 👈 Yeh line zaroor jodh lena User model ke liye
from .models import Task

# 1. Aapka purana Task Serializer (Bilkul jaisa aapne bheja)
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'user', 'title', 'description', 'is_completed', 'created_at', 'updated_at']
        read_only_fields = ['user']  

    def validate_title(self, value):
        if len(value.strip()) < 5:
            raise serializers.ValidationError("Bhai, title kam se kam 5 characters ka hona chahiye!")
        if value.isdigit():
            raise serializers.ValidationError("Bhai, title me sirf ginti nahi chalegi!")
        return value


# 2. 👇 YEH HAI NAYA ADDITION (Jo normal user ka account banayega)
class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def create(self, validated_data):
        # User.objects.create_user use karne se password automatic hash/encrypt ho jata hai
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        return user