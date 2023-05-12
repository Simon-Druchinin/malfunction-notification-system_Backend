from django.urls import path
from schemas import views


urlpatterns = (
    path('items/', views.ItemList.as_view()),
    path('item-categories/', views.ItemCategoryList.as_view()),
    path('room-schemas/', views.RoomSchemaList.as_view()),
    path('room-schemas/<int:pk>/', views.RoomSchemaDetail.as_view()),
    path('room-schemas/create/', views.RoomSchemaCreate.as_view()),
    path('room-item/', views.RoomItemCreate.as_view())
)
