from rest_framework import serializers
from .models import User, Admin
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'first_name', 
            'last_name', 
            'email', 
            'phone', 
            'occupation',
            'address', 
            'last_bus_stop', 
            'state', 
            'visiting', 
            'gender', 
            'id']
   

class UserSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'first_name', 
            'last_name', 
            'occupation', 
            'email', 
            'phone', 
            'address', 
            'last_bus_stop', 
            'state', 
            'visiting', 
            'gender', 
            'id'
        ]

class AdminSignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Admin
        fields = ('username', 'password', 'first_name', 'last_name', 'email')