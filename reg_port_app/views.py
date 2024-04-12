from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from .serializers import UserSerializer, UserSearchSerializer, AdminSignUpSerializer
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token

class UserList(APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

class UserDetail(APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, users_id):
        user = User.objects.get(id=users_id)
        serializer = UserSerializer(user)
        return Response(serializer.data)


class UserCreate(APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class UserUpdate(APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def put(self, request, users_id):
        user = User.objects.get(id=users_id)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)


class UserDelete(APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def delete(self, request, users_id):
        user = User.objects.get(id=users_id)
        user.delete()
        return Response(status=204)
    


class UserSearchView(viewsets.ModelViewSet):
    serializer_class = UserSearchSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        first_name = self.request.query_params.get('first_name', None)
        last_name = self.request.query_params.get('last_name', None)

        if first_name is not None:
            queryset = queryset.filter(first_name__icontains=first_name)
        if last_name is not None:
            queryset = queryset.filter(last_name__icontains=last_name)

        return queryset
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    

class AdminSignUpAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = AdminSignUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# admins/views.py
from django.contrib.auth import authenticate  # Import the authenticate function

class AdminLoginAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        # Authenticate user
        admin = authenticate(username=username, password=password)

        if admin is None:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        # If authentication is successful, create or get the token
        token, _ = Token.objects.get_or_create(user=admin)
        return Response({'token': token.key}, status=status.HTTP_200_OK)


class AdminLogoutAPIView(APIView):
    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)