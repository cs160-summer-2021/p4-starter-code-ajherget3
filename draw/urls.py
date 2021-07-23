# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('userscreen', views.userscreen, name='userscreen'),
    path('<str:room_name>/', views.room, name='room'),

]
