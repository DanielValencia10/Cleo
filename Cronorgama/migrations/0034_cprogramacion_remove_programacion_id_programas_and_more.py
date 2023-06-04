# Generated by Django 4.2 on 2023-05-29 00:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Cronorgama', '0033_bdcontratista_grupo_remove_programacion_dia_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cprogramacion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('programacion', models.ManyToManyField(related_name='cprogramacion', to='Cronorgama.casignatura')),
            ],
        ),
        migrations.RemoveField(
            model_name='programacion',
            name='id_programas',
        ),
        migrations.AddField(
            model_name='programacion',
            name='bdcontratista',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='Cronorgama.bdcontratista'),
        ),
        migrations.AddField(
            model_name='programacion',
            name='grupo',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='Cronorgama.grupo'),
        ),
        migrations.CreateModel(
            name='itinerario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('activo', models.BooleanField(default=True)),
                ('cprogramacion', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='programaciones', to='Cronorgama.cprogramacion')),
                ('programa', models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='Cronorgama.programas')),
            ],
        ),
    ]