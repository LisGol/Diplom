# Generated by Django 3.2.9 on 2022-02-14 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0002_auto_20211126_0910'),
    ]

    operations = [
        migrations.RenameField(
            model_name='history',
            old_name='Year',
            new_name='year',
        ),
    ]
