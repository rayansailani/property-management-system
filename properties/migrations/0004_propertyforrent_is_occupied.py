# Generated by Django 3.1.1 on 2020-11-19 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0003_auto_20201117_1910'),
    ]

    operations = [
        migrations.AddField(
            model_name='propertyforrent',
            name='is_occupied',
            field=models.BooleanField(default=False),
        ),
    ]
