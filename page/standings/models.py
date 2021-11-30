from django.db import models


class country(models.Model):
    country = models.CharField(max_length=200, db_index=True, verbose_name='Страны')

    class Meta:
        ordering = ('country',)
        verbose_name = 'Личный зачет'
        verbose_name_plural = 'Личный зачет'

    def __str__(self):
        return self.country


class team(models.Model):
    team = models.CharField(max_length=200, db_index=True, verbose_name='Команда')

    class Meta:
        ordering = ('team',)
        verbose_name = 'Личный зачет'
        verbose_name_plural = 'Личный зачет'

    def __str__(self):
        return self.team


class Team_standing(models.Model):
    team = models.ForeignKey(team, blank=True,on_delete=models.SET_NULL, null=True)
    country = models.ForeignKey(country, blank=True,on_delete=models.SET_NULL, null=True)
    point = models.CharField(max_length=200, db_index=True, verbose_name='Очки')

    class Meta:
        ordering = ('point',)
        verbose_name = 'Личный зачет'
        verbose_name_plural = 'Личный зачет'

    def __str__(self):
        return self.point


class Personal_standing(models.Model):
    team = models.ForeignKey(team, blank=True, on_delete=models.SET_NULL, null=True)
    country = models.ForeignKey(country, blank=True, on_delete=models.SET_NULL, null=True)
    driver = models.CharField(max_length=200, db_index=True, verbose_name='Гонщик')
    point = models.CharField(max_length=200, db_index=True, verbose_name='Очки')

    class Meta:
        ordering = ('driver',)
        verbose_name = 'Личный зачет'
        verbose_name_plural = 'Личный зачет'

    def __str__(self):
        return self.driver