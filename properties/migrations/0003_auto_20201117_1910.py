# Generated by Django 3.1.1 on 2020-11-17 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0002_auto_20201117_1729'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='propertyforrent',
            options={'verbose_name': 'Property', 'verbose_name_plural': 'Properties for Rent'},
        ),
    ]