from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


# 1. CUSTOM USER MODEL
class User(AbstractUser):
    ROLE_CHOICES = (
        ('manager', 'Project Manager'),
        ('developer', 'Developer'),
    )
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='developer')

    USERNAME_FIELD = 'email'  # Log in using email instead of username
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f"{self.email} ({self.role})"


# 2. PROJECT MODEL
class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='managed_projects')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# 3. TASK MODEL
class Task(models.Model):
    STATUS_CHOICES = (
        ('todo', 'To Do'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    )
    PRIORITY_CHOICES = (
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    )

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todo')
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='medium')
    assigned_to = models.ManyToManyField(User, related_name='assigned_tasks', blank=True)
    due_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title