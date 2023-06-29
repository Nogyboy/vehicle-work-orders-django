from django.urls import path
from .views import client_vehicles, create_vehicle, update_vehicle

urlpatterns = [
    path('client/', client_vehicles),
    path('create/', create_vehicle),
    path('update/<int:pk>/', update_vehicle),
]
