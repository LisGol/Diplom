from django.contrib import admin
from . import models


@admin.register(models.Team_standing)
class Team_standingAdmin(admin.ModelAdmin):
    list_display = ('team', 'point1')


@admin.register(models.Personal_standing)
class Personal_standingAdmin(admin.ModelAdmin):
    list_display = ('team', 'point', 'driver')
    filter = ('-point')