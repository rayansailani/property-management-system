# Generated by Django 3.1.3 on 2020-11-21 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0006_auto_20201121_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertyforrent',
            name='image1',
            field=models.ImageField(default='house.jpeg', upload_to='house_images/'),
        ),
        migrations.AlterField(
            model_name='propertyforrent',
            name='image2',
            field=models.ImageField(default='house.jpeg', upload_to='house_images/'),
        ),
        migrations.AlterField(
            model_name='propertyforrent',
            name='image3',
            field=models.ImageField(default='house.jpeg', upload_to='house_images/'),
        ),
        migrations.AlterField(
            model_name='propertyforrent',
            name='image4',
            field=models.ImageField(default='house.jpeg', upload_to='house_images/'),
        ),
    ]
