from django.shortcuts import render
from products.models import *


def one_product(request, product_cat, product_id):
    product = Products.objects.get(id=product_id)

    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    print(request.session.session_key)

    return render(request, 'products/product.html', locals())
