# Generated by Django 4.0 on 2021-12-23 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_category_remove_destination_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='category',
            field=models.ManyToManyField(to='main.Category'),
        ),
    ]
