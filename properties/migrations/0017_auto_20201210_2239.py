# Generated by Django 3.1.3 on 2020-12-10 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0016_auto_20201210_1201'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appointment',
            options={'verbose_name': 'Appointment ', 'verbose_name_plural': 'Appointments for sale property'},
        ),
        migrations.AlterModelOptions(
            name='visit',
            options={'verbose_name': 'Appointment ', 'verbose_name_plural': 'Appointments for rental property'},
        ),
        migrations.AddField(
            model_name='propertyforrent',
            name='description',
            field=models.TextField(default=' ', max_length=1000),
        ),
        migrations.AddField(
            model_name='propertyforsale',
            name='description',
            field=models.TextField(default=' ', max_length=1000),
        ),
    ]
