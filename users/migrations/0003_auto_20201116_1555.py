# Generated by Django 3.1.1 on 2020-11-16 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_propertyforrent'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='owners',
            options={'verbose_name': 'Owner', 'verbose_name_plural': 'Owners'},
        ),
        migrations.AlterModelOptions(
            name='propertyforrent',
            options={'verbose_name': 'Property', 'verbose_name_plural': 'Properties'},
        ),
        migrations.RenameField(
            model_name='propertyforrent',
            old_name='location',
            new_name='address',
        ),
    ]
