from django.urls import path
from . import views

app_name = 'autontification'


urlpatterns = [
    path('registration/', views.registration, name='registration'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
