from django.urls import path

from page.history import views

app_name = 'history'

urlpatterns = [
    path('history/', views.list_history, name='History'),
    path('history/<slug:period_slug>/', views.single_history, name='Period')
]
# news/<slug:news_slug>