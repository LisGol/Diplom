from django.urls import path

from page.history import views

app_name = 'history'

urlpatterns = [
    path('', views.list_history, name='history'),
    path('history/<slug:period_slug>/', views.single_history, name='period')
]
