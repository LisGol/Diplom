from django.shortcuts import render

from page.team.models import Car, DriverR, DriverL


def car(request):
    car = Car.objects.filter()
    return render(request,
                  'diplom/team/car.html',
                  {'car': car})


def driver_russell(request):
    driverR = DriverR.objects.all()
    return render(request,
                  'diplom/team/russell.html',
                  {'driverR': driverR})


def driver_latifi(request):
    driverL = DriverL.objects.all()
    return render(request,
                  'diplom/team/latify.html',
                  {'driverL': driverL})

