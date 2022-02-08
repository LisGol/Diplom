from django.contrib import admin

from page.news.models import News
from user.cart.models import Order

from user.comments.models import Comment, OrderItem


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    # raw_id_fields = ('product')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    # list_display = ('id', 'first_name', 'last_name', 'email',
    #                     'address', 'postal_code', 'city', 'paid',
    #                     'created', 'updated')
    #
    # list_filter = ('paid', 'created', 'updated')
    # inlines = [OrderItemInline]
    pass