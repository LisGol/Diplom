from django.contrib import admin

# Register your models here.
from user.cart import models


@admin.register(models.Cart)
class CartAdmin(admin.ModelAdmin):
     pass


class OrderAdmin(admin.ModelAdmin):
    pass

class CustomerAdmin(admin.ModelAdmin):
    pass


class CartImageInline(admin.StackedInline):
   pass