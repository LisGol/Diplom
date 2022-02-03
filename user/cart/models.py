from django.db import models
from django.contrib.auth.models import User

from django.conf import settings


class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)


class CartProduct(models.Model):
    product = models.ForeignKey('shop.Product', on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE, null=True)
    quantity = models.PositiveIntegerField(default=1)


class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, unique=True)


class Order(models.Model):
    user = models.ForeignKey('Customer', on_delete=models.CASCADE)
    products = models.ManyToManyField('CartProduct')
    # start_date = models.DateTimeField(auto_now_add=True, default=True)
    ordered_date = models.DateTimeField(default=True)
    ordered = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username

class Item(models.Model):
    title = models.CharField


# from django.db import models
#
# from diplom import settings
#
#
# class Customer(models.Model):
#     full_name = models.CharField(verbose_name='name')
#     phone_number = models.CharField(verbose_name='number')
#     email = models.EmailField(verbose_name='email')
#
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#
#
# class Cart(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     created = models.DateTimeField(auto_now=True)
#     checked_out = models.BooleanField(default=False)
#
#
# class CartProduct(models.Model):
#     product = models.ForeignKey('page.Product', on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField()
#     cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
#
#
# class Order(models.Model):
#     user = models.ForeignKey('Customer', on_delete=models.CASCADE)
#     products = models.ManyToManyField('CartProduct')
#     date = models.DateField(auto_now=True)
