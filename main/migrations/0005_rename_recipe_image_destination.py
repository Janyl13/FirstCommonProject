# Generated by Django 4.0 on 2021-12-23 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='recipe',
            new_name='destination',
        ),
    ]
