from django.db.utils import IntegrityError
from rest_framework import serializers
from schemas.models import ItemCategory, Item, RoomSchema, RoomItem

from drf_writable_nested.serializers import WritableNestedModelSerializer


class ItemCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemCategory
        fields = ('id', 'name', 'zIndex')


class ItemSerializer(serializers.ModelSerializer):
    category = ItemCategorySerializer()
    
    class Meta:
        model = Item
        fields = ('id', 'name', 'characteristics', 'type', 'category')

class RoomItemSerializer(serializers.ModelSerializer):
    item = ItemSerializer(read_only=True)
    
    class Meta:
        model = RoomItem
        fields = ('id', 'x', 'y', 'item')
    
    def to_representation(self, instance):
        instance = super().to_representation(instance)
        item = instance.pop('item')
        instance = {**item, **instance}
        
        return instance

class RoomItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = RoomItem
        fields = ('id', 'x', 'y', 'item', 'room_schema')

class RoomSchemaNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomSchema
        fields = ('id', 'name')
        
class RoomSchemaSerializer(WritableNestedModelSerializer):
    items = RoomItemSerializer(many=True)
    
    class Meta:
        model = RoomSchema
        fields = ('id', 'name', 'length', 'width', 'items')  

class RoomSchemaCreateSerializer(WritableNestedModelSerializer):
    class Meta:
        model = RoomSchema
        fields = ('id', 'name', 'length', 'width')      
