from django.shortcuts import render, get_object_or_404

from page.team.models import Team

def car (request):
    car = Team.objects.all()
    return render(request,
                  'diplom/team/car.html',
                  {'car': car})


def driver_russell(request):
    driverR= Team.objects.all()
    return render(request,
                  'diplom/team/russell.html',
                  {'driverR': driverR})

def driver_latify(request):
    driverL = Team.objects.all()
    return render(request,
                  'diplom/team/latify.html',
                  {'driverL': driverL})

