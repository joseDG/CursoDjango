# Generated by Django 5.0.3 on 2024-03-15 00:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departamentos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=60, verbose_name='Nombres')),
                ('last_name', models.CharField(max_length=60, verbose_name='Apellidos')),
                ('job', models.CharField(choices=[('0', 'Contador'), ('1', 'Administrador'), ('2', 'Economista'), ('3', 'Otro')], max_length=1, verbose_name='Puesto de Trabajo')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departamentos.departamento')),
            ],
        ),
    ]
