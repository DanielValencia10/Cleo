# Generated by Django 4.2 on 2023-05-13 18:59

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Cronorgama', '0009_remove_disponibilidad_profesor_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cdia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a', models.BooleanField(default=0)),
                ('b', models.BooleanField(default=0)),
                ('c', models.BooleanField(default=0)),
                ('d', models.BooleanField(default=0)),
                ('e', models.BooleanField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Cdisponibilidad',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cdia', models.ManyToManyField(related_name='cdia', to='Cronorgama.cdia')),
            ],
        ),
        migrations.CreateModel(
            name='Dia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='Disponibilidad',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_inicio', models.DateTimeField(default=datetime.datetime.now)),
                ('fecha_fin', models.DateTimeField(default=datetime.datetime(2023, 5, 20, 13, 59, 5, 63210))),
                ('Profesor', models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('cdisponibilidad', models.ManyToManyField(related_name='cdisponibilidad', to='Cronorgama.cdisponibilidad')),
            ],
        ),
        migrations.AddField(
            model_name='cdia',
            name='dia',
            field=models.ForeignKey(blank=True, default='', max_length=200, on_delete=django.db.models.deletion.CASCADE, to='Cronorgama.dia'),
        ),
    ]
