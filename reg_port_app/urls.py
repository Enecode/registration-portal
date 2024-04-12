from django.urls import path, include
from .views import UserList, UserDetail, UserCreate, UserUpdate, UserDelete, UserSearchView, AdminSignUpAPIView, AdminLoginAPIView, AdminLogoutAPIView

urlpatterns = [
    path('users/', UserList.as_view()),
    path('user-detail/<int:users_id>/', UserDetail.as_view()),
    path('users/create/', UserCreate.as_view()),
    path('users/<int:users_id>/update/', UserUpdate.as_view()),
    path('users/<int:users_id>/delete/', UserDelete.as_view()),

    path('search/', UserSearchView.as_view({'get':'list'})),

   
    path('admin/signup/', AdminSignUpAPIView.as_view(), name='admin_signup'),
    path('admin/login/', AdminLoginAPIView.as_view(), name='admin_login'),
    path('admin/logout/', AdminLogoutAPIView.as_view(), name='admin_logout'),
]