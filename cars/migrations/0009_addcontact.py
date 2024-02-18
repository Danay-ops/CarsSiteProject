# Generated by Django 5.0.1 on 2024-02-18 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0008_cars_author_alter_cars_cat_alter_cars_content_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.CharField(max_length=200)),
            ],
        ),
    ]
