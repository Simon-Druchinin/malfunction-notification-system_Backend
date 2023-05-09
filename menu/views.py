from menu.models import NavigationMenu, DropDownMenu
from menu.serializers import NavigationMenuSerializer, DropDownMenuSerializer
from rest_framework import generics, filters


class NavigationMenuList(generics.ListAPIView):
    queryset = NavigationMenu.objects.filter(parent_id=None)
    serializer_class = NavigationMenuSerializer
    
class DropDownMenuList(generics.ListAPIView):
    queryset = DropDownMenu.objects.all()
    serializer_class = DropDownMenuSerializer
