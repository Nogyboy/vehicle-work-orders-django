from django.urls import path
from rest_framework.authtoken import views
from .views import custom_user_detail, custom_user_list

urlpatterns = [
    path('login/', views.obtain_auth_token),
    path('users/', custom_user_list),
    path('users/<int:pk>/', custom_user_detail),
]
