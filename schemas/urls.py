from django.urls import path
from schemas import views


urlpatterns = (
    path('items/', views.ItemList.as_view()),
    path('item-categories/', views.ItemCategoryList.as_view()),
)
