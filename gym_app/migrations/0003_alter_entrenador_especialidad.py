# Generated by Django 5.2 on 2025-04-16 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym_app', '0002_categoria_entrenador_apellido_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrenador',
            name='especialidad',
            field=models.CharField(choices=[('halterofilia', 'Halterofilia'), ('gimnasio', 'Gimnasio'), ('metcon', 'Metcon'), ('crossfit', 'CrossFit')], max_length=20),
        ),
    ]
