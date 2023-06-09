# Generated by Django 4.2 on 2023-05-15 13:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Cronorgama', '0022_asignaturaxprofesor_casigxprofe_cdia_cdisponibilidad_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casigxprofe',
            name='hora_finClase',
            field=models.TimeField(blank=True, verbose_name='Hora fin'),
        ),
        migrations.AlterField(
            model_name='casigxprofe',
            name='hora_inicioClase',
            field=models.TimeField(blank=True, verbose_name='Hora de inicio'),
        ),
        migrations.CreateModel(
            name='MensajesDisponibilidad',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('mensaje', models.CharField(max_length=300)),
                ('activo', models.BooleanField(default=True)),
                ('confirmar', models.BooleanField(default=True)),
                ('disponibilidad', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='Cronorgama.disponibilidad')),
                ('usuario_emisor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mensajes_disponibilida_enviado', to=settings.AUTH_USER_MODEL)),
                ('usuarios_destinatarios', models.ManyToManyField(related_name='mensajes_disponibilidad_recibidos', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
