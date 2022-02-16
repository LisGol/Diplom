from django.contrib import admin

from . import models
from .models import ProductImage


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(models.Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class ProductImageAdmin(admin.ModelAdmin):
    pass


class ProductImageInline(admin.StackedInline):
    model = ProductImage
    max_num = 10
    extra = 0


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'gender', 'price', 'stock', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductImageInline]
    admin.site.register(ProductImage, ProductImageAdmin)

