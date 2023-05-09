from django.urls import path
from menu import views


urlpatterns = (
    path('nav-menu/', views.NavigationMenuList.as_view()),
    path('dropdown-menu/', views.DropDownMenuList.as_view()),
)
