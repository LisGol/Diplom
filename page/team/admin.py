from django.contrib import admin
from . import models
from .models import TeamImage, Team


class TeamImageAdmin(admin.ModelAdmin):
    pass


class TeamImageInline(admin.StackedInline):
    model = TeamImage
    max_num = 10
    extra = 0


@admin.register(models.Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('rank'),
    inlines = [TeamImageInline]
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(TeamImage, TeamImageAdmin)


@admin.register(models.Rank)
class RankAdmin(admin.ModelAdmin):
    pass