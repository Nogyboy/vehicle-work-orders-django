from rest_framework import serializers
from .models import Vehicle

class ClientVehiclesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['id', 'plate', 'brand', 'model', 'year', 'color', 'image']

class CreateVehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['plate', 'brand', 'model', 'year', 'color', 'image']
