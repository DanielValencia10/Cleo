# Generated by Django 4.2 on 2023-05-29 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cronorgama', '0035_alter_cprogramacion_programacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='cdia',
            name='activo',
            field=models.BooleanField(default=True),
        ),
    ]