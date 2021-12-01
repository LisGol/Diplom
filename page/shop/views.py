from django.http import HttpResponse
from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def catalog (request):
    categories = Category.objects.all()
    return render(request, 'diplomproject/shop/category.html',
                    # 'shop/list.html',
                    {"categories": categories,})

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


def category_view(request, category_id):
    categories = Category.objects.get(id=category_id)
    if category_id:
         category = get_object_or_404(Category, id=category_id)
    return render(request,
                  'diplomproject/shop/category.html',
                   # {'category': category,
                  { 'categories': categories})

def product_detail(request, product_id):
    product = Category.objects.get(id=product_id)
    if product_id:
        product = get_object_or_404(Product, id=product_id)
    return render(request,
                  'shop/list.html',
                  {'product': product})


