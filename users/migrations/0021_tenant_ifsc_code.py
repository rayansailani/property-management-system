# Generated by Django 3.1.3 on 2020-11-22 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0020_auto_20201121_1441'),
    ]

    operations = [
        migrations.AddField(
            model_name='tenant',
            name='ifsc_code',
            field=models.CharField(default='xxxxxxxxxxx', max_length=11),
        ),
    ]
