from django.utils import timezone

from rest_framework import serializers
from schemas.models import (ItemCategory, Item, RoomSchema, 
                            RoomItem, MalfunctionReport, MalfunctionReportStatus, MalfunctionReportItem)

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

class MalfunctionReportStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = MalfunctionReportStatus
        fields = ('id', 'name', )

class MalfunctionReportItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MalfunctionReportItem
        fields = ('problem_text', 'malfunction_report', 'room_element')

class MalfunctionReportSerializer(WritableNestedModelSerializer):
    status = serializers.HiddenField(default=MalfunctionReportStatus.objects.get(pk=1))
    date_created = serializers.HiddenField(default=timezone.now)
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = MalfunctionReport
        fields = ('id', 'name', 'problem_text', 'room_schema', 'date_created', 'created_by', 'status')
