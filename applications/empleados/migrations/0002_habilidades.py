# Generated by Django 5.0.3 on 2024-03-15 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habilidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habilidad', models.CharField(max_length=50, verbose_name='Habilidades')),
            ],
        ),
    ]
