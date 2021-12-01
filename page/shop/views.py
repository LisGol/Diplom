from django.http import HttpResponse
from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def catalog (request):
    catalog = Category.objects.all()
    return render(request, 'shop/catalog.html',
                         {"catalog": catalog})

#
# def category_view(request, category_id):
#     cat = Category.objects.get(id=category_id)
#     return HttpResponse(cat.name)
    # products = Product.objects.filter(available=True)
    # if category_slug:
    #     category = get_object_or_404(Category, slug=category_slug)
    #     products = products.filter(category=category)

                  # 'diplomproject/shop/category.html',
                  # {'category': category,
                  #  'categories': categories,
                  #  'products': products})


def category_view(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    return render(request,
                  'shop/category.html',
                  {'category': category})


def product(request, product_slug):
    product = get_object_or_404(Category, slug=product_slug)
    return render(request,
                  'shop/product.html',
                  {'product': product})









