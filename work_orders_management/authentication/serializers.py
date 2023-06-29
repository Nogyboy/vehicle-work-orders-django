from rest_framework import serializers
from django.contrib.auth.models import User
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']

class CustomUserSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = CustomUser
        fields = ['user', 'is_cliente', 'is_administrador']
