from django.urls import path
from . import views

app_name = 'cal'
urlpatterns = [
    path('', views.home_view, name="home"),
    path('calendar/', views.CalendarView.as_view(), name='calendar'),
    # path('event/new/', views.event, name='event_new'),
    path('event/edit/(?P<event_id>\d+)/', views.home_view, name='event_edit'),
    path('delete/<int:pk>/', views.delete, name='todos-delete'),

]
