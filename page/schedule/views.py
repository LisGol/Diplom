from django.shortcuts import render

from page.schedule.models import Schedule


def schedule(request):
    schedule = Schedule.objects.order_by("date").all()
    date = schedule.filter(date__range=["28.03", "12.12"])
    return render(request, 'diplom/schedule/schedule.html',
                  {'schedule': schedule,
                   'date': date})
