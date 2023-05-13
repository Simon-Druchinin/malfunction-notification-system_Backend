from uuid import uuid4

from django.db import transaction
from django.conf import settings
from django.contrib.auth.models import Group, Permission
from django.core.validators import validate_email

from rest_framework import serializers
from rest_framework.validators import ValidationError

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer

from users.models import User
from users.utils import django_permission_to_casl_ability


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ('codename',)

class GroupSerializer(serializers.ModelSerializer):
    permissions = PermissionSerializer(many=True, read_only=True)
    class Meta:
        model = Group
        fields = ('id', 'name', 'permissions')

class UserSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'groups')

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Добавляем пользовательские данные в токен
        token['user_data'] = get_user_data(user)

        return token

class CustomTokenRefreshSerializer(TokenRefreshSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = super().token_class(data["refresh"])
        user = User.objects.get(pk=refresh["user_data"]["id"])

        refresh["user_data"] = get_user_data(user)

        data = {"access": str(refresh.access_token)}

        refresh.set_jti()
        refresh.set_exp()
        refresh.set_iat()

        data["refresh"] = str(refresh)

        return data
    
class UserCreateSerializer(serializers.ModelSerializer):
    group_id = serializers.IntegerField(write_only=True)
    
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'password', 'group_id')
    
    def validate(self, attrs):
        validate_email(attrs['email'])
        email_exists=User.objects.filter(email=attrs['email']).exists()
        if email_exists:
            raise ValidationError('Этот email адрес уже занят')
        return super().validate(attrs)
    
    def create(self, validated_data):
        group_id = validated_data.pop('group_id')
        password = validated_data.pop('password')
        validated_data['username'] = uuid4().hex[:32].upper()
        
        if group_id == 1:
            validated_data['is_staff'] = True
            validated_data['is_superuser'] = True
        
        with transaction.atomic():
            user: User = super().create(validated_data)

            user.set_password(password)
            user.save()

            user.groups.add(group_id)

        return user

def get_user_data(user: User):
    serializer = UserSerializer(user)
    user_data = serializer.data
    print(user_data)
    permissions = user_data['groups'][0].pop('permissions')
    
    user_data['ability'] = django_permission_to_casl_ability(permissions, user)
    print(user.is_staff)
    return user_data
