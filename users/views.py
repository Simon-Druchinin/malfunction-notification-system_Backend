from django.contrib.auth.models import Group

from rest_framework import generics

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.models import User
from users.permissions import CustomDjangoModelPermissions
from users.serializers import (CustomTokenObtainPairSerializer, CustomTokenRefreshSerializer, UserCreateSerializer, GroupSerializer)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class CustomTokenRefreshView(TokenRefreshView):
    serializer_class = CustomTokenRefreshSerializer

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = (CustomDjangoModelPermissions, )

class GroupList(generics.ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (CustomDjangoModelPermissions, )
