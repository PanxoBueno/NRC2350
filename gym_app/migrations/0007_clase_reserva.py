# Generated by Django 5.2 on 2025-04-17 15:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym_app', '0006_alter_biblioteca_descripcion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('horario', models.CharField(choices=[('06:00', '06:00 AM'), ('07:00', '07:00 AM'), ('08:00', '08:00 AM'), ('17:00', '05:00 PM'), ('18:00', '06:00 PM'), ('19:00', '07:00 PM')], max_length=5)),
                ('fecha', models.DateField()),
                ('capacidad_maxima', models.PositiveIntegerField(default=15)),
                ('entrenador', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gym_app.entrenador')),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_reserva', models.DateTimeField(auto_now_add=True)),
                ('atleta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym_app.atleta')),
                ('clase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym_app.clase')),
            ],
            options={
                'unique_together': {('atleta', 'clase')},
            },
        ),
    ]
