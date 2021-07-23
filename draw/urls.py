# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('user', views.user, name='user'),
    path('<str:room_name>/', views.room, name='room'),

]
