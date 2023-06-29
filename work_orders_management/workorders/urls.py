from django.urls import path
from .views import client_work_orders_active

urlpatterns = [
    path('client/active/', client_work_orders_active, name='work-orders-client-active'),
]
