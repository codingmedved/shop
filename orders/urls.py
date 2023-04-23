from django.contrib import admin
from django.urls import path, include
from orders import views

urlpatterns = [
    # path('landing', views.landing, name='landing'),
    path('basket_adding', views.basket_adding, name='basket_adding'),
    path('checkout', views.checkout, name='checkout'),

]
