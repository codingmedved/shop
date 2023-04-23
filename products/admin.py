from django.contrib import admin
from .models import *


class ProductsImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0


class ProductsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Products._meta.fields]
    inlines = [ProductsImageInline]

    class Meta:
        model = Products


admin.site.register(Products, ProductsAdmin)


class ProductsCategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductsCategory._meta.fields]

    class Meta:
        model = ProductsCategory


admin.site.register(ProductsCategory, ProductsCategoryAdmin)


class ProductImageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductImage._meta.fields]

    class Meta:
        model = ProductImage


admin.site.register(ProductImage, ProductImageAdmin)
