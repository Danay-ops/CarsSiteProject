# Generated by Django 5.0.1 on 2024-02-04 12:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_categories_cars_cat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='cat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cars.categories'),
        ),
    ]
