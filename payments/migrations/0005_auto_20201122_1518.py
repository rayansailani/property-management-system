# Generated by Django 3.1.3 on 2020-11-22 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0004_auto_20201122_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentpayment',
            name='month_of',
            field=models.DateField(auto_now_add=True),
        ),
    ]
