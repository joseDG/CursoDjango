# Generated by Django 5.0.3 on 2024-03-22 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='prueba',
            name='cantidad',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]