from django.shortcuts import render, get_object_or_404

from page.news.models import News
from django.views.generic import ListView

from user.comments.forms import CommentForm


class ListNews(ListView):
    model = News
    template_name = 'diplom/news/list.html'
    context_object_name = 'news'
    extra_context = {'title': 'Новости'}

    def get_queryset(self):
        return News.objects.all()


def single_news(request, post_slug):
    post = get_object_or_404(News, slug=post_slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request,
                  'diplom/news/blog-single.html',
                  {'post': post,
                   'comments': comments,
                   'new_comment': new_comment,
                   'comment_form': comment_form,
                })


def last_article():
    last_pages = News.objects.order_by("-id")[0:3]
    return {
        'last_pages': last_pages,
    }
