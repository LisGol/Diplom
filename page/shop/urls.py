from django.conf import settings

from django.conf.urls.static import static
from django.urls import path
from page.shop import views


app_name = 'shop'


urlpatterns = [
        path('', views.CatalogList.as_view(), name='shop'),
        path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
        path('<int:id>/<slug:slug>/', views.product, name='product_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
