# Generated by Django 5.0.1 on 2024-02-03 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_cars_slug_alter_cars_time_create'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]
