# Generated by Django 3.1.1 on 2020-11-20 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20201119_1829'),
    ]

    operations = [
        migrations.AddField(
            model_name='tenant',
            name='start_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
