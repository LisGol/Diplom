from django.db import models


class TeamStanding(models.Model):
    team = models.CharField(max_length=50, blank=True, null=True, verbose_name='Команда')
    score = models.DecimalField(max_digits=4, decimal_places=1, db_index=True, verbose_name='Очки')

    class Meta:
        ordering = ('team',)
        verbose_name = 'Командный зачет'
        verbose_name_plural = 'Командный зачет'

    def __str__(self):
        return self.team


class PersonalStanding(models.Model):
    team = models.CharField(max_length=50, blank=True, null=True, verbose_name='Команда')
    driver = models.CharField(max_length=200, db_index=True, verbose_name='Гонщик')
    point = models.DecimalField(max_digits=4, decimal_places=1, db_index=True, verbose_name='Очки')

    class Meta:
        ordering = ('driver',)
        verbose_name = 'Личный зачет'
        verbose_name_plural = 'Личный зачет'

    def __str__(self):
        return self.driver