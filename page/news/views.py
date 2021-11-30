from django.shortcuts import render, get_object_or_404

from page.news.models import News


def list_news(request):
    news = News.objects.all()
    return render(request,
                  'diplom/news/list.html',
                  {'news': news})


def single_news(request, post_slug):
    post = get_object_or_404(News, slug=post_slug)

    return render(request,
                  'diplom/news/blog-single.html',
                  {'post': post})
