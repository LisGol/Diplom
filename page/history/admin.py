from django.contrib import admin
from . import models
from .models import HistoryImage


class HistoryImageAdmin(admin.ModelAdmin):
  pass


class HistoryImageInline(admin.StackedInline):
  model = HistoryImage
  max_num=10
  extra=0


@admin.register(models.History)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = [HistoryImageInline]
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(HistoryImage, HistoryImageAdmin)

@admin.register(models.Year)
class YearAdmin(admin.ModelAdmin):
    pass