# Generated by Django 3.0.3 on 2021-01-22 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diaries', '0009_auto_20201227_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oneliners',
            name='oneliners_image',
            field=models.ImageField(blank=True, null=True, upload_to='oneliners'),
        ),
        migrations.AlterField(
            model_name='poems',
            name='poems_image',
            field=models.ImageField(blank=True, null=True, upload_to='poems'),
        ),
        migrations.AlterField(
            model_name='shayri',
            name='shayri_image',
            field=models.ImageField(blank=True, null=True, upload_to='shayri'),
        ),
    ]
