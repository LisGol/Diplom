# Generated by Django 3.2.9 on 2021-12-17 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20211116_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, max_length=3000, verbose_name='Описание'),
        ),
    ]
