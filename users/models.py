from os.path import splitext

from uuid import uuid4

from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, Group
from django.core.validators import validate_email


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        validate_email(email)
        username = uuid4().hex[:32].upper()

        user = self.model(
            email=email,
            username=username,
            **extra_fields
        )

        user.set_password(password)
        user.save()
        
        if extra_fields.get('is_superuser'):
            admin_group = Group.objects.get(name='Администратор')
            user.groups.add(admin_group)
        else:
            teacher_group = Group.objects.get(name='Преподаватель')
            user.groups.add(teacher_group)

        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser has to have is_staff set to True")
        
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser has to have is_superuser set to True")
        
        return self.create_user(email=email, password=password, **extra_fields)

class User(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)

    objects = CustomUserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ('first_name', 'last_name')

    def __str__(self):
        return f'{self.last_name} {self.first_name}'
