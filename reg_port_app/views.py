from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, AdminSerializer 
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Admin
from rest_framework.response import Response
from rest_framework import generics, permissions

class UserRegistrationAPIView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RegisterView(APIView):
  def post(self, request):
    serializer = AdminSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

class LoginView(TokenObtainPairView):
  queryset = Admin.objects.all()


class LogoutView(APIView):
  def post(self, request):
    return Response({'detail': 'Successfully logged out.'}, status=status.HTTP_205_RESET_CONTENT)
  

class UserSearchAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        query = self.request.query_params.get('query', None)
        if query:
            queryset = User.objects.filter(
                models.Q(first_name__icontains=query) |
                models.Q(last_name__icontains=query) |
                models.Q(email__icontains=query) |
                models.Q(phone__icontains=query)
            )
        else:
            queryset = User.objects.all()
        return queryset