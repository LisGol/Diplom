from django.contrib import admin
from . import models


@admin.register(models.country)
class CountryAdmin(admin.ModelAdmin):
    pass


@admin.register(models.team)
class Team_Admin(admin.ModelAdmin):
    pass


@admin.register(models.Team_standing)
class Team_standingAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Personal_standing)
class Personal_standingAdmin(admin.ModelAdmin):
    pass