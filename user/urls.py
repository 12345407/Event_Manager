from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView

from .views import login_view, register_view, reg_otp_view

urlpatterns = [
    path('signin/', login_view, name='login'),
    path('signup/', register_view, name='register'),
    path('signup/otp', reg_otp_view, name='otp'),
    path('logout', LogoutView.as_view(), name="logout"),
]
