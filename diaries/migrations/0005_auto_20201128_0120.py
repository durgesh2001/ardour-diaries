# Generated by Django 3.0.8 on 2020-11-27 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diaries', '0004_auto_20201128_0055'),
    ]

    operations = [
        migrations.RenameField(
            model_name='oneliners',
            old_name='poem_image',
            new_name='oneliners_image',
        ),
        migrations.RenameField(
            model_name='poems',
            old_name='poem_image',
            new_name='poems_image',
        ),
        migrations.RenameField(
            model_name='shayri',
            old_name='poem_image',
            new_name='shayri_image',
        ),
    ]
