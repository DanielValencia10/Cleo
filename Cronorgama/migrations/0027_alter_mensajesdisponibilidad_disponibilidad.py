# Generated by Django 4.2 on 2023-05-27 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Cronorgama', '0026_salon_habilitado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensajesdisponibilidad',
            name='disponibilidad',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='Cronorgama.disponibilidad'),
        ),
    ]