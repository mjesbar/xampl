from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('room/', views.room, name='room'),
    path('variable/', views.variable, name='variable'),
    path('extend/', views.extend, name='extend'),
]
