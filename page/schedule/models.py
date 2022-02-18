from django.db import models


class Schedule(models.Model):
    date = models.DateField(auto_now=False)
    image = models.ImageField(upload_to='schedule', blank=True, verbose_name='Фото')
    grandprix = models.CharField(max_length=200, db_index=True, verbose_name='Гран При')
    track = models.CharField(max_length=200, db_index=True, verbose_name='Трасса')
    length = models.CharField(max_length=10, verbose_name='Длина')
    laps = models.IntegerField(verbose_name='Круги')
    distance = models.DecimalField(max_digits=10, decimal_places=3, verbose_name='Дистанция')
    winner = models.CharField(max_length=200, db_index=True, verbose_name='Победитель')
    team = models.CharField(max_length=200, db_index=True, verbose_name='Команда')

    class Meta:
        ordering = ('grandprix',)
        verbose_name = 'Календарь'
        verbose_name_plural = 'Календарь'

    def __str__(self):
        return self.grandprix or 'date'


