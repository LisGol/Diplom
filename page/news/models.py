from django.urls import reverse
from django.utils import timezone
from django.db import models
# from mptt.models import MPTTModel, TreeForeignKey
from user.autontification.models import User


class Tag(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    slug = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэг'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('news', kwargs={'news_slug': self.slug})


STATUS_CHOICES = (('опубликован', 'Опубликован'), ('не опубликован', 'Не опубликован'))


class News(models.Model):
    title = models.CharField(max_length=1000, verbose_name='Название')
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='articles/', verbose_name='Фото')
    publish = models.DateTimeField(default=timezone.now, verbose_name='Дата публикации')
    author = models.ForeignKey(User, related_name='news', on_delete=models.CASCADE, verbose_name='Автор', null=True)
    text = models.TextField(verbose_name='Текст')
    tags = models.ManyToManyField(Tag, related_name='news', verbose_name='Тэг')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата обнавления')
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='опубликован', verbose_name='Статус')

    class Meta:
        ordering = ('title',)
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news:post', args=[self.slug])
