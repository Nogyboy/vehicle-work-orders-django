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

class UpdateVehicleSerializer(serializers.ModelSerializer):
    plate = serializers.CharField(max_length=10, required=False)

    class Meta:
        model = Vehicle
        fields = '__all__'

    def get_fields(self):
        fields = super().get_fields()
        if self.partial and 'plate' not in self.initial_data:
            fields['plate'].required = False
        return fields
