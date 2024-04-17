from django.urls import path, include
from .views import UserSignUpAPIView, UserSearchView, AdminSignUpAPIView, AdminLoginAPIView, AdminLogoutAPIView

urlpatterns = [
    path('users/', UserSignUpAPIView.as_view()),
    # path('user-details/', UserDetails.as_view()),

    path('search/', UserSearchView.as_view({'get':'list'})),
   
    path('admin/signup/', AdminSignUpAPIView.as_view(), name='admin_signup'),
    path('admin/login/', AdminLoginAPIView.as_view(), name='admin_login'),
    path('admin/logout/', AdminLogoutAPIView.as_view(), name='admin_logout'),
]