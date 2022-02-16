from django.db.models import Prefetch, Count

from page.shop.models import Category, Product

from django.shortcuts import render, get_object_or_404

from django.views.generic import ListView

from user.cart.models import CartProduct


class CatalogList(ListView):
    model = Category
    template_name = 'shop/catalog.html'
    context_object_name = 'catalog'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.annotate(Count('product'))
        context['title'] = 'Магазин'
        return context


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                    'shop/category.html',
                   {'category': category,
                    'categories': categories,
                    'products': products})


class CartAddPtoductForm:
    pass


def product(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddPtoductForm()
    is_in_cart = CartProduct.objects.filter(
        product=product,
        cart__user=request.user,
        cart__active=True).first()
    return render(request,
                    'shop/product.html',
                    {'product': product,
                     'is_in_cart': is_in_cart})
