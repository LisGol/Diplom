from django.shortcuts import render

from page.schedule.models import Schedule


def schedule(request):
    schedule = Schedule.objects.order_by("date").all
    return render(request, 'diplom/schedule/schedule.html',
                  {'schedule': schedule,
                   })

