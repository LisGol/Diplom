from django.urls import path
from . import views

app_name = 'team'


urlpatterns = [
    path('driver_russell/', views.driver_russell, name='driver_R'),
    path('driver_latify/', views.driver_latifi, name='driver_l'),
    path('car/', views.car, name='car'),
]