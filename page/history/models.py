from django.db import models

from django.db import models
from django.urls import reverse


class Year(models.Model):
    name = models.CharField(max_length=500, verbose_name='Период')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Период'
        verbose_name_plural = 'Период'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('history', kwargs={'history_slug': self.slug})


class History(models.Model):
    title = models.CharField(max_length=500, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    Year = models.ForeignKey(Year, blank=True,on_delete=models.SET_NULL, null=True)
    slug = models.CharField(max_length=500, verbose_name='Название', null=True, blank=True)

    class Meta:
        ordering = ('title',)
        verbose_name = 'История'
        verbose_name_plural = 'История'

    def get_absolute_url(self):
        return reverse('history:Period', args=[self.slug])

    def __str__(self):
        return self.title


class HistoryImage(models.Model):
    image = models.ImageField(upload_to='history')
    description = models.TextField(max_length=1000, blank=True, verbose_name='Описание')
    history = models.ForeignKey(History, blank=True, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ('image',)
        verbose_name = 'Фото для истории'
        verbose_name_plural = 'Фото для истории'

    def __str__(self):
        return self.description
