# Generated by Django 3.2.9 on 2021-12-17 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='image',
            field=models.ImageField(blank=True, upload_to='schedule', verbose_name='Фото'),
        ),
    ]
