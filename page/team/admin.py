from django.contrib import admin
from . import models
from .models import TeamImage


class TeamImageAdmin(admin.ModelAdmin):
    pass


class TeamImageInline(admin.StackedInline):
    model = TeamImage
    max_num = 10
    extra = 0


@admin.register(models.Car)
class CarAdmin(admin.ModelAdmin):
    inlines = [TeamImageInline]
    prepopulated_fields = {'slug': ('name',)}
    admin.site.register(TeamImage, TeamImageAdmin)


@admin.register(models.DriverL)
class DriverLAdmin(admin.ModelAdmin):
    inlines = [TeamImageInline]
    prepopulated_fields = {'slug': ('name',)}


@admin.register(models.DriverR)
class DriverRAdmin(admin.ModelAdmin):
    inlines = [TeamImageInline]
    prepopulated_fields = {'slug': ('name',)}