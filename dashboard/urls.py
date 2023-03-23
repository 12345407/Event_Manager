from django.contrib import admin
from django.urls import path, include

from .views import home_view, task_view

urlpatterns = [
    path('', home_view, name="home"),
    path('task/', task_view, name='task'),

]
