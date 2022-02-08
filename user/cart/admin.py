from django.contrib import admin

from user.cart import models


@admin.register(models.Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user']


