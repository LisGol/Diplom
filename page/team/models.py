from django.db import models


class Rank (models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='Наименование')
    #slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Team(models.Model):
    rank = models.ForeignKey(Rank, blank=True, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200, db_index=True, verbose_name='Наименование')
    slug = models.SlugField(max_length=200, db_index=True, null=True)
    text = models.TextField(max_length=3000, blank=True)
    description = models.TextField(max_length=1000, blank=True, verbose_name='Описание')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Команда'

    def __str__(self):
        return self.name


class TeamImage(models.Model):
    image = models.ImageField(upload_to='team')
    team = models.ForeignKey(Team, blank=True, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ('image',)
        verbose_name = 'Фото для истории'

    # def __str__(self):
    #     return self.image