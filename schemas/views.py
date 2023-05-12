from rest_framework import generics, filters, status
from rest_framework.response import Response

from schemas.models import ItemCategory, Item, RoomSchema, RoomItem
from schemas.serializers import (ItemCategorySerializer, 
                                 ItemSerializer, 
                                 RoomSchemaSerializer, 
                                 RoomSchemaNameSerializer,
                                 RoomItemCreateSerializer,
                                 RoomSchemaCreateSerializer)


class ItemCategoryList(generics.ListAPIView):
    queryset = ItemCategory.objects.all()
    serializer_class = ItemCategorySerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['zIndex']
    ordering = ['zIndex']
    
    
class ItemList(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class RoomSchemaList(generics.ListAPIView):
    queryset = RoomSchema.objects.all()
    serializer_class = RoomSchemaNameSerializer

class RoomSchemaCreate(generics.CreateAPIView):
    queryset = RoomSchema.objects.all()
    serializer_class = RoomSchemaCreateSerializer
    
class RoomSchemaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RoomSchema.objects.all()
    serializer_class = RoomSchemaSerializer

class RoomItemCreate(generics.CreateAPIView):
    queryset = RoomItem.objects.all()
    serializer_class = RoomItemCreateSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
