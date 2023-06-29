from rest_framework import serializers
from vehicles.models import Vehicle
from .models import WorkOrders
from vehicles.serializers import ClientVehiclesSerializer



class VehicleWorkOrdersActiveSerializer(serializers.ModelSerializer):
    vehicle = ClientVehiclesSerializer(read_only=True)

    class Meta:
        model = WorkOrders
        fields = ['id', 'vehicle', 'start_date', 'end_date', 'description', 'status']