from django.db import models


class Team_standing(models.Model):
    team = models.CharField(max_length=50, blank=True, null=True, verbose_name='Команда')
    point1 = models.CharField(max_length=200, db_index=True, verbose_name='Очки')

    class Meta:
        ordering = ('point1',)
        verbose_name = 'Командный зачет'
        verbose_name_plural = 'Командный зачет'

    def __str__(self):
        return self.point1


class Personal_standing(models.Model):
    team = models.CharField(max_length=50, blank=True, null=True, verbose_name='Команда')
    driver = models.CharField(max_length=200, db_index=True, verbose_name='Гонщик')
    point = models.CharField(max_length=200, db_index=True, verbose_name='Очки')

    class Meta:
        ordering = ('point',)
        verbose_name = 'Личный зачет'
        verbose_name_plural = 'Личный зачет'

    def __str__(self):
        return self.driver