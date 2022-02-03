import os
import uuid

from django.db import models

from django.db import models


# Category name=магазин
    # Man
        # SubcategoryMan
            # Футболки
                # Футболка №1
                # Футболка №2
            # Кепки...
                # Кепка №1
    # women
        # Subcategorywomen
                # куртки
                    # куртка №1
                    # куртка №2
                # шорты
                    # шорты №1
    # kids
        # #Subcategorykids
                # штаны
                    # штаны №1
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='Наименование')
    slug = models.SlugField(max_length=200, db_index=True)
    # parent = models.ForeignKey('self', verbose_name='Подкатегория', on_delete=models.PROTECT, null=True, blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])


class Subcategory(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='Наименование')
    slug = models.SlugField(max_length=200, db_index=True)
    # category = models.ForeignKey(Category, related_name="subcategories", on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_slug': self.slug})



GENDER_CHOICES = (('Мужчинам', 'Мужчинам'), ('Женщинам', 'Женщинам'), ('Детям', 'Детям'), ('Сувениры', 'Сувениры'))
SIZE_CHOICES = (('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('2XL', '2XL'), ('one size', 'one size'))


class Product(models.Model):
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    # Subcategory = models.ForeignKey(Subcategory, blank=True, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, db_index=True, verbose_name='Наименование')
    slug = models.SlugField(max_length=200, db_index=True)
    description = models.TextField(max_length=3000, blank=True, verbose_name='Описание')
    details = models.TextField(max_length=200, blank=True, verbose_name='Характеристика')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default="male")
    size = models.CharField(max_length=20, choices=SIZE_CHOICES)
    quantity = models.PositiveIntegerField(default=1, verbose_name='Колличество')
    stock = models.PositiveIntegerField(verbose_name='Оставшееся количество', null=True, blank=True)
    available = models.BooleanField(default=True, verbose_name='Доступность товара')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Время создания', null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, verbose_name='Время последнего обнавления')

    class Meta:
        verbose_name = 'Продукты'
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
         return reverse('shop:product_detail',
                        args=[self.id, self.slug])

    # def get_absolute_url(self):
    #     return reverse('shop:product', kwargs={'product_slug': self.slug})

# def __str__(self):
    #     return f'{self.name} {{self.price}}'
class ProductImage(models.Model):
    image = models.ImageField(upload_to='products')
    product = models.ForeignKey(Product, blank=True, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ('image',)
        verbose_name = 'Фото для магазина'

    def __str__(self):
        return str(self.image)

''' отвечает за вывод каталога (мужское, женское ...)'''

def get_absolute_url(self):
    return reverse('shop:category', args=[self.slug])

