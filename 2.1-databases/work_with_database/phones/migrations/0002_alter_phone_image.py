# Generated by Django 4.2.6 on 2023-11-17 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='image',
            field=models.URLField(verbose_name='Изображение'),
        ),
    ]
