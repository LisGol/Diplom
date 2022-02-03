from urllib import request

from django.shortcuts import render, get_object_or_404

from page.shop.models import Product
from user.cart.models import Cart, CartProduct


def add_to_cart(request, product_slug,):
    product = get_object_or_404(Product, slug=product_slug)

    is_new_cart=False
    cart = Cart.objects.get_or_create(user=request.user, checked_out=False)
    # if not cart:
    #     is_new_cart = True
    #     cart = Cart()
    # if is_new_cart:
    cart_product = CartProduct.objects.get_or_create(prodict=product, cart=cart)
    if cart_product in cart.cartproduct_set:
        cart_product.quantity += 1
    else:
        cart.cartproduct_set.add(cart_product)


def cart(request):
    user = request.user
    customer