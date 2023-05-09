from schemas.models import ItemCategory, Item
from schemas.serializers import ItemCategorySerializer, ItemSerializer
from rest_framework import generics


class ItemCategoryList(generics.ListAPIView):
    queryset = ItemCategory.objects.all()
    serializer_class = ItemCategorySerializer
    
class ItemList(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
