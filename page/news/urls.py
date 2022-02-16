from django.urls import path

from page.news import views
from page.news.views import ListNews

app_name = 'news'

urlpatterns = [
    path('', ListNews.as_view(), name='news'),
    path('news/<slug:post_slug>/', views.single_news, name='post')
]
