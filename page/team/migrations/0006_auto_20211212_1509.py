# Generated by Django 3.2.9 on 2021-12-12 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0005_auto_20211212_1448'),
    ]

    operations = [
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=200, verbose_name='Наименование')),
            ],
        ),
        migrations.AlterModelOptions(
            name='driverl',
            options={'ordering': ('name',), 'verbose_name': 'L', 'verbose_name_plural': 'L'},
        ),
        migrations.AlterModelOptions(
            name='driverr',
            options={'ordering': ('name',), 'verbose_name': 'R', 'verbose_name_plural': 'R'},
        ),
        migrations.AddField(
            model_name='driverl',
            name='title',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='team.title'),
        ),
        migrations.AddField(
            model_name='driverr',
            name='title',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='team.title'),
        ),
    ]
