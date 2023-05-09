from rest_framework import serializers
from schemas.models import ItemCategory, Item


class ItemCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemCategory
        fields = ('name', )


class ItemSerializer(serializers.ModelSerializer):
    item_category = ItemCategorySerializer()
    
    class Meta:
        model = Item
        fields = ('id', 'name', 'characteristics', 'item_type', 'item_category', )
    
