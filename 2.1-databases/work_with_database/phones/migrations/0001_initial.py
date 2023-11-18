# Generated by Django 4.2.6 on 2023-11-01 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='Модель')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Стоимость')),
                ('image', models.BinaryField(verbose_name='Изображение')),
                ('release_date', models.DateField(verbose_name='Дата выхода')),
                ('lte_exists', models.BooleanField()),
                ('slug', models.SlugField(verbose_name='URL')),
            ],
        ),
    ]
