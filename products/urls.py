from django.contrib import admin
from django.urls import path, include
from products import views

urlpatterns = [
    path('<slug:product_cat>/<int:product_id>', views.one_product, name='product'),
]
