from django.conf import settings
from django.conf.urls import url
from page.shop.views import category_view
from django.conf.urls.static import static
from django.urls import path, include, re_path
from . import views


app_name = 'shop'


urlpatterns = [

       path('shop/', views.catalog, name='shop'),
       path('/<slug:category_slug>/', views.category_view, name='category_view'),
       path('category/<slug:product_slug>/', views.product, name='product_detail'),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
