from django.shortcuts import render

from page.schedule.models import Schedule


def schedule(request):
    schedule = Schedule.objects.all()
    return render(request, 'diplom/schedule/schedule.html',
                  {'schedule': schedule,
                   })
