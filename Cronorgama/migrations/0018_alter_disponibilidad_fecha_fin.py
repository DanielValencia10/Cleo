# Generated by Django 4.2 on 2023-05-15 06:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cronorgama', '0017_alter_disponibilidad_fecha_fin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disponibilidad',
            name='fecha_fin',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 22, 1, 19, 0, 957791)),
        ),
    ]
