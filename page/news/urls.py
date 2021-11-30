from django.urls import path

from page.news import views

app_name = 'news'

urlpatterns = [
    path('news/', views.list_news, name='News'),
    path('news/<slug:post_slug>/', views.single_news, name='post')
]
