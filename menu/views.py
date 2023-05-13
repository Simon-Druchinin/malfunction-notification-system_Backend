from django.db.models import Q

from menu.models import NavigationMenu, DropDownMenu
from menu.serializers import NavigationMenuSerializer, DropDownMenuSerializer
from rest_framework import generics, filters

from users.models import User
from users.utils import get_user_permissions

class NavigationMenuList(generics.ListAPIView):
    serializer_class = NavigationMenuSerializer
    
    def get_queryset(self):
        user: User = self.request.user
        user_permissions = get_user_permissions(user)
        user_permissions_ids = [permission.id for permission in user_permissions]
        
        return NavigationMenu.objects.filter(parent_id=None).filter(Q(permission__in=user_permissions_ids) | Q(permission=None))
    
class DropDownMenuList(generics.ListAPIView):
    serializer_class = DropDownMenuSerializer
    
    def get_queryset(self):
        user: User = self.request.user
        user_permissions = get_user_permissions(user)
        user_permissions_ids = [permission.id for permission in user_permissions]
        
        return DropDownMenu.objects.filter(Q(permission__in=user_permissions_ids) | Q(permission=None))
