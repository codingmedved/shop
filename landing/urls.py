from django.contrib import admin
from django.urls import path, include
from landing import views

urlpatterns = [
    path('', views.home, name='home'),
    path('landing', views.landing, name='landing'),
]
