

from django.shortcuts import render, get_object_or_404

from page.news.models import News
from django.views.generic import ListView


class ListNews(ListView):
    model = News
    template_name = 'diplom/news/list.html'
    context_object_name = 'news'
    extra_context = {'title': 'Новости'}

    def get_queryset(self):
        return News.objects.all()


def single_news(request, post_slug):
    post = get_object_or_404(News, slug=post_slug)

    return render(request,
                  'diplom/news/blog-single.html',
                  {'post': post})




