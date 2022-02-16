from django.shortcuts import render, get_object_or_404

from page.history.models import History


def list_history(request):
    history = History.objects.all()
    return render(request,
                  'diplom/history/history.html',
                  {'history': history})


def single_history(request, period_slug):
    period = get_object_or_404(History, slug=period_slug)

    return render(request,
                  'diplom/history/singlhistory.html',
                  {'period': period})


