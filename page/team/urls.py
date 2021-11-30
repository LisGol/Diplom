from django.urls import path
from . import views

app_name = 'Team'


urlpatterns = [
    path('driver_russell/', views.driver_russell, name='Driver_R'),
    path('driver_latify/', views.driver_latify, name='Driver_l'),
    path('car/', views.car, name='Car'),
]