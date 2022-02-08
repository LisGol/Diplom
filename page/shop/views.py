from django.contrib.auth.decorators import login_required
from django.db.models import Prefetch, Count

from page.shop.models import Category, Product
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from django.views.generic import ListView, DetailView

from user.cart.models import CartProduct


class CatalogList(ListView):
    model = Category
    template_name = 'shop/catalog.html'
    context_object_name = 'catalog'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.annotate(Count('product'))
        #     context['title'] = 'Магазин'
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
    # cart_product_form = CartAddPtoductForm()
    is_in_cart = CartProduct.objects.filter(
        product=product,
        cart__user=request.user,
        cart__active=True).first()
    return render(request,
                    'shop/product.html',
                    {'product': product,
                     'is_in_cart': is_in_cart})
                     # 'cart_product_form':cart_product_form})

# def product_view(request: WSGIRequest, product_slug: str):
#     print('product_slug = ', product_slug)
#     try:
#         product = (
#             Product.objects
#                 .get(slug=product_slug)
#                 .prefetch_related('product_set')
#                 .filter(slug=product_slug)
#                 .first()
#         )
#         print(product)
#         is_in_cart = CartProduct.objects.filter(
#             product=product,
#             cart__user=request.user,
#             cart__active=True).first()
#
#         context = {
#             'product': product,
#              'is_in_cart': is_in_cart,
#         }
#     except Product.DoesNotExist:
#         raise Http404
#     return render(
#         request, 'shop/product.html',
#         context
#     )
#
#
# def category_list(request: WSGIRequest, category_slug: str):
#     try:
#         category = (
#             Category.objects
#             # .prefetch_related('product_set')
#             .filter(slug=category_slug)
#             .first()
#     )
#     except Category.DoesNotExist:
#         raise Http404
#     return render(
#         request, 'shop/category.html',
#         {"category": category})



# 
# def product (request, id):
#     product = Product.objects.get(pk=id)
#     context = {
#         'product': product
#     }
#     session_key = request.session.session_key
#     if not session_key:
#         request.session["session_key"]=123
#         request.session.cycle_key()
#         print(request.session.session_key)
#     return render (request,'shop/product.html', context)

# class ShowProduct(DetailView):
#     model = Product
#     template_name = 'shop/product.html'
#     slug_url_kwarg = 'product_slug'
#     context_object_name = 'product'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = context['product']
#         return context


# def shop (request):
#     product = Product.objects.all()
#     context = {
#         'pr': product
#     }
#     return render (request,'shop/category.html', context)
# class CategoryList(ListView):
#     model = Product
#     template_name = 'shop/category.html'
#     context_object_name = 'category'
#     allow_empty = False
#
#     def get_queryset(self):
#         return Product.objects.filter(category__slug=self.kwargs['category_slug'])
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Категория'
#         context['category_selected'] = context['category']
#         return context




# class ProductList(ListView):
#     model = Product
#     template_name = 'shop/category.html'
#     context_object_name = 'productlist'
#
#     # def get_queryset(self):
#     #     return Product.objects.filter(=["muzhchinam","suveniry"])


    # def get_querset(self):
    #     category = get_object_or_404(Category, slug=self.kwargs.get('slug'))
    #     return category.product_set.all()

    # def get_context_data(self, **kwargs):
    #     context = super(ProductList, self).get_context_data(**kwargs)
    #
    #     context['Мужчинам'] = get_object_or_404(Category, slug='muzhchinam')
    #     context['Сувениры'] = get_object_or_404(Category, slug='suveniry')
    #
    #     context["muzhchinam_product_list"] = self.get_queryset().filter(category=context['Мужчинам'])
    #     context["suveniry_product_list"] = self.get_queryset().filter(category=context['Сувениры'])
    #
    #     return context
#
# class ShowProduct(DetailView):
#     model = Product
#     template_name = 'shop/pr.html'
#     slug_url_kwarg = 'product_slug'
#     context_object_name = 'product'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = context['product']
#         return context


# def category_view(request: WSGIRequest, category_slug: str, children=None, parent=None, subcategory=None):
#     # cat = Category.objects.all()
#     product = Product.objects.all
#     category = Category.objects.filter()
#     return render(
#             request,
#             'shop/category.html',
#             {'category': category},
#         {'product': product})
#             # {'cat': cat})
#
# #

# def category_view(request):
#     cat = Category.objects.all()
#     context = {'cat': cat}
#     return render(request, 'shop/category.html', context)

# def category_view(request, category_slug):
#     cat = Category.objects.get(slug=category_slug)
#     return HttpResponse(cat.name)
#     products = Product.objects.filter(cat=cat)
#     if category_slug:
#         category = get_object_or_404(Category, slug=category_slug)
#         products = products.filter(category=category)
#         return render(request, 'shop/category.html',
#                       {'cat': category,
#                        # 'categories': categories,
#                        'products ': products})



# def product(request, product_slug):
#
#     return render(request,
#                   'shop/category.html',
#                   {'product': product})
# #
# def subcategory(request, subcategory_slug):
#     subcategory = get_object_or_404(Subcategory, slug=subcategory_slug)
#     products = Product.objects.filter(subcategory=product)
#     return render(request,
#                   'shop/subcategory.html',
#                    {'subcategory': subcategory})
#                    # 'souvenir': category,
#                    # 'kid': category,
#                    # 'men': category,
#                    # 'women': category})
#
#
#


# def category_view(request, category_slug, parent_category=None, slug=None, subcategory=None, subcategory_slug=None,
#                   subcategory_id=None):
#     category = get_object_or_404(Category, slug=category_slug)
#     products= Product.objects.filter(category=product)
#     # categories= Category.objects.filter(parent_category=category)
#     return render(request,
#                   'shop/category.html',
#                   {'category': category,
#                    'product':products})
#                    # 'souvenir': category,
#                    # 'kid': category,
#                    # 'men': category,
#                    # 'women': category})



#
# def product(request, category_slug=None):
#     category = None
#     categories = Category.objects.all()
#     products = Product.objects.filter(available=True).order_by('-created')
#     if category_slug:
#         category = get_object_or_404(Category, slug=category_slug)
#         sub_categories = category.get_descendants(include_self=True)
#         products = products.filter(category__in=sub_categories)
#     return render(request,
#                   'shop/product.html',
#                   {'category': category,
#                   'categories': categories,
#                    'products': products})
