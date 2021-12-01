from django.conf import settings
from django.conf.urls import url
from page.shop.views import category_view
from django.conf.urls.static import static
from django.urls import path, include, re_path
from . import views


app_name = 'shop'

# urlpatterns = [
#     path('', views.product_list,
#          views.product_detail),
# ]
#     #path('category/<int:category_id>/',)
#
# ](r'^(?P<category_slug>[-\w]+)/$',
urlpatterns = [
    #  url(r'^$', views.product_list, name='product_list'),
    # re_path(r'^shop/(?P<pk>\d+)$', views.product_list, name='product_list_by_category'),
    # # re_path(г'^ shop/ (? P <заглушка> [- \ w] +) $', views.product_list, name]
    # url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
    #      views.product_detail,
    #      name='product_detail'),
       path('', views.catalog, name='shop'),
       path('category/<int:category_id>/', views.category_view, name='category_view'),
       path('product/<int:product_id>/', views.product_detail, name='product_detail'),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
