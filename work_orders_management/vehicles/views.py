from rest_framework.permissions import IsAuthenticated
from .models import Vehicle
from .serializers import ClientVehiclesSerializer, CreateVehicleSerializer, UpdateVehicleSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

# Get all vehicles from the current user
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def client_vehicles(request):
    vehicles = Vehicle.objects.filter(user=request.user)
    serializer = ClientVehiclesSerializer(vehicles, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# Create a new vehicle for the current user
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_vehicle(request):
    serializer = CreateVehicleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Update a vehicle
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_vehicle(request, pk):
    vehicle = Vehicle.objects.get(id=pk)
    serializer = UpdateVehicleSerializer(instance=vehicle, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)