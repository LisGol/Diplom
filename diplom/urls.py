"""diplom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from diplom import settings
from page.home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', include('page.shop.urls'), name='shop'),
    path('', views.HomeTemplateView.as_view(), name='Home'),
    path('', include('page.news.urls', namespace='news')),
    path('', include('page.history.urls')),
    path('', include('page.schedule.urls')),
    path('', include('user.autontification.urls')),
    path('', include('page.standings.urls')),
    path('', include('page.team.urls')),
    path('cart', include('user.cart.urls')),
    path('orders/', include('user.comments.urls', namespace='orders')),
]



if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)