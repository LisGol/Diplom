from django.contrib import admin
from . import models


@admin.register(models.Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('grandprix', 'date')
    list_filter = ('winner', 'team')
