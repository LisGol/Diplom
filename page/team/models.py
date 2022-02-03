from django.db import models


class Car(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='Наименование')
    slug = models.SlugField(max_length=200, db_index=True, null=True)
    text = models.TextField(max_length=10000, blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class DriverL(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='Наименование')
    slug = models.SlugField(max_length=200, db_index=True, null=True)
    text = models.TextField(max_length=10000, blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'L'
        verbose_name_plural = 'L'

    def __str__(self):
        return self.name


class DriverR(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='Наименование')
    slug = models.SlugField(max_length=200, db_index=True, null=True)
    text = models.TextField(max_length=10000, blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'R'
        verbose_name_plural = 'R'

    def __str__(self):
        return self.name


class TeamImage(models.Model):
    image = models.ImageField(upload_to='team')
    car = models.ForeignKey(Car, blank=True, on_delete=models.CASCADE, null=True)
    driverR = models.ForeignKey(DriverR, blank=True, on_delete=models.CASCADE, null=True)
    driverL = models.ForeignKey(DriverL, blank=True, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ('image',)
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'

    def __str__(self):
        return str(self.image)

