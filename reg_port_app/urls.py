from django.urls import path, include
from .views import UserRegistrationAPIView, RegisterView, LoginView, LogoutView, UserSearchAPIView
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    # path('register/', UserRegistrationAPIView.as_view(), name='user-registration'),

    path('admin/search/', UserSearchAPIView.as_view(), name='user-search'),

    path('admin/register/', RegisterView.as_view(), name='register'),
    path('admin/login/', LoginView.as_view(), name='login'),
    path('admin/logout/', LogoutView.as_view(), name='logout'),
]