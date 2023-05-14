from rest_framework import generics, filters, status
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend

from users.permissions import CustomDjangoModelPermissions

from schemas.models import ItemCategory, Item, RoomSchema, RoomItem, MalfunctionReportItem, MalfunctionReport
from schemas.serializers import (ItemCategorySerializer, 
                                 ItemSerializer, 
                                 RoomSchemaSerializer, 
                                 RoomSchemaNameSerializer,
                                 RoomItemCreateSerializer,
                                 RoomSchemaCreateSerializer,
                                 MalfunctionReportCreateSerializer,
                                 MalfunctionReportItemCreateSerializer,
                                 MalfunctionReportSerializer, MalfunctionReportListSerializer)


class ItemCategoryList(generics.ListAPIView):
    queryset = ItemCategory.objects.all()
    serializer_class = ItemCategorySerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['zIndex']
    ordering = ['zIndex']
    
    
class ItemList(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = (CustomDjangoModelPermissions, )

class RoomSchemaList(generics.ListAPIView):
    queryset = RoomSchema.objects.all()
    serializer_class = RoomSchemaNameSerializer
    permission_classes = (CustomDjangoModelPermissions, )

class RoomSchemaCreate(generics.CreateAPIView):
    queryset = RoomSchema.objects.all()
    serializer_class = RoomSchemaCreateSerializer
    permission_classes = (CustomDjangoModelPermissions, )
    
class RoomSchemaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RoomSchema.objects.all()
    serializer_class = RoomSchemaSerializer
    permission_classes = (CustomDjangoModelPermissions, )

class RoomItemCreate(generics.CreateAPIView):
    queryset = RoomItem.objects.all()
    serializer_class = RoomItemCreateSerializer
    permission_classes = (CustomDjangoModelPermissions, )
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class MalfunctionReportCreate(generics.CreateAPIView):
    queryset = MalfunctionReport.objects.all()
    serializer_class = MalfunctionReportCreateSerializer

class MalfunctionReportItemCreate(generics.CreateAPIView):
    queryset = MalfunctionReportItem.objects.all()
    serializer_class = MalfunctionReportItemCreateSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class MalfunctionReportList(generics.ListAPIView):
    queryset = MalfunctionReport.objects.all()
    serializer_class = MalfunctionReportListSerializer
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    ordering = ['-date_created']
    filterset_fields = ['created_by', 'taken_by']
    
class MalfunctionReportDetailUpdate(generics.RetrieveUpdateAPIView):
    queryset = MalfunctionReport.objects.all()
    serializer_class = MalfunctionReportSerializer
    
class MalfunctionReportTake(generics.UpdateAPIView):
    queryset = MalfunctionReport.objects.all()
    serializer_class = MalfunctionReportCreateSerializer
