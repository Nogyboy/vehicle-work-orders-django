from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from .models import WorkOrders
from .serializers import VehicleWorkOrdersActiveSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

# Get all active work orders from the current user
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def client_work_orders_active(request):
    work_orders = WorkOrders.objects.filter(vehicle__user=request.user).exclude(status='F')
    serializer = VehicleWorkOrdersActiveSerializer(work_orders, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
