# Generated by Django 3.2.9 on 2021-12-21 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('standings', '0007_auto_20211215_1233'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='personal_standing',
            options={'ordering': ('point',), 'verbose_name': 'Личный зачет', 'verbose_name_plural': 'Личный зачет'},
        ),
    ]
