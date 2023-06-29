from rest_framework import permissions
from .models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework import status

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if the authenticated user is an administrator
        if request.user.is_authenticated and request.user.customuser.is_administrador:
            return True
        
        return False

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated, IsAdmin])
def custom_user_list(request):
    queryset = CustomUser.objects.all()
    serializer = CustomUserSerializer(queryset, many=True)
    
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def custom_user_detail(request, pk):
    try:
        user = CustomUser.objects.get(pk=pk)
    except CustomUser.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = CustomUserSerializer(user)
    return Response(serializer.data)
