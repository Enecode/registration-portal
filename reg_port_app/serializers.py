from rest_framework import serializers
from .models import User, Admin
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
   

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

class AdminSerializer(serializers.ModelSerializer):
  class Meta:
    model = Admin
    fields = ['id', 'first_name', 'last_name', 'email', 'username', 'password']
    extra_kwargs = {'password': {'write_only': True}}  # Ensure password is write-only

  def create(self, validated_data):
    password = validated_data.pop('password')
    validated_data['password'] = make_password(password)  # Hash password before saving
    return Admin.objects.create(**validated_data)
