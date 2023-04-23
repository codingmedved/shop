from django.shortcuts import render
from .forms import SubscriberForm
from products.models import *


def landing(request):
    name = 'CodingMedved'
    form = SubscriberForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()

    return render(request, 'landing/landing.html', locals())


def home(request):
    products_images = ProductImage.objects.filter(is_active=True, product__is_active=True).order_by('?')
    products_images_phones = products_images.filter(product__category__name__contains='Phones')
    products_images_laptops = products_images.filter(product__category__name__contains='Laptops')
    return render(request, 'landing/home.html', locals())
