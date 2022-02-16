from django.contrib import admin
from . import models


@admin.register(models.TeamStanding)
class TeamStandingAdmin(admin.ModelAdmin):
    list_display = ('team', 'score')


@admin.register(models.PersonalStanding)
class PersonalStandingAdmin(admin.ModelAdmin):
    list_display = ('team', 'point', 'driver')
    filter = ('-point')