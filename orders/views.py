from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render
from .forms import CheckoutContactForm

from .models import *


def basket_adding(request):
    return_dict = dict()
    session_key = request.session.session_key
    data = request.POST
    product_id = data.get('product_id')
    num = data.get('num')
    is_delete = data.get('is_delete')

    if is_delete == 'true':
        ProductInBasket.objects.filter(id=product_id).update(is_active=False)
    else:
        new_product, created = ProductInBasket.objects.get_or_create(session_key=session_key, product_id=product_id,
                                                                     is_active=True,
                                                                     defaults={'number': num})
        if not created:
            new_product.number += int(num)
            new_product.save(force_update=True)

    products_in_cart = ProductInBasket.objects.filter(session_key=session_key, is_active=True)
    return_dict['products_total_numb'] = products_in_cart.count()
    return_dict['products'] = list()

    for item in products_in_cart:
        products_dict = dict()
        products_dict['id'] = item.id
        products_dict['name'] = item.product.name
        products_dict['price_per_item'] = item.price_per_item
        products_dict['num'] = item.number
        return_dict['products'].append(products_dict)

    return JsonResponse(return_dict)


def checkout(request):
    session_key = request.session.session_key
    products_in_cart = ProductInBasket.objects.filter(session_key=session_key, is_active=True, order__isnull=True)
    form = CheckoutContactForm(request.POST or None)
    if request.POST:
        print(request.POST)
        if form.is_valid():
            data = request.POST
            name = data.get('name', 'None')
            phone = data['phone']
            user, created = User.objects.get_or_create(username=phone, defaults={'first_name': name})

            order = Orders.objects.create(user=user, customer_name=name, customer_phone=phone, status_id=None)

            for k, v in data.items():
                if k.startswith('product_'):
                    product_in_cart_id = k.split('_')[1]
                    product_in_cart = ProductInBasket.objects.get(id=product_in_cart_id)
                    product_in_cart.number = int(v)
                    product_in_cart.order = order
                    product_in_cart.save(force_update=True)

                    ProductInOrder.objects.create(product=product_in_cart.product, number=product_in_cart.number,
                                                  price_per_item=product_in_cart.price_per_item,
                                                  total_price=product_in_cart.total_price, order=order)
        else:
            print('NO')
    return render(request, 'orders/checkout.html', locals())
