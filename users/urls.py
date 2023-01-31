from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import UserRegistrationView, LoginProfileView, UserProfileView, logout

app_name = 'users'

urlpatterns = [
    path('<int:pk>', login_required(UserProfileView.as_view()), name='profile'),
    path('registration/', UserRegistrationView.as_view(), name='register'),
    path('login/', LoginProfileView.as_view(), name='login'),
    path('logout/', logout.as_view(), name='logout'),
]