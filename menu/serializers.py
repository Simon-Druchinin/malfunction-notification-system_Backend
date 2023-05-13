from collections import OrderedDict

from rest_framework import serializers
from menu.models import NavigationMenu, DropDownMenu


class ChildNavigationMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = NavigationMenu
        exclude = ('parent', 'permission')


class NavigationMenuSerializer(serializers.ModelSerializer):
    children = ChildNavigationMenuSerializer(many=True, read_only=True)
    class Meta:
        model = NavigationMenu
        fields = ('id', 'title', 'icon', 'navLink', 'children', )
    
    def to_representation(self, instance):
        result = super(NavigationMenuSerializer, self).to_representation(instance)
        return OrderedDict([(key, result[key]) for key in result if result[key] != []])

class DropDownMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = DropDownMenu
        fields = '__all__'
