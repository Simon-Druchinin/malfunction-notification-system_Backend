from django.urls import path
from users import views


urlpatterns = (
    path('create/', views.UserCreate.as_view()),
    path('groups/', views.GroupList.as_view()),
)
