# Generated by Django 4.2 on 2023-06-05 04:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Cronorgama', '0037_user_cedula'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tapoyoxprograma',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Tapoyo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('programa', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Cronorgama.programas')),
            ],
        ),
    ]
