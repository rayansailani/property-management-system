# Generated by Django 3.1.3 on 2020-11-22 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0005_auto_20201122_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentpayment',
            name='transaction_id',
            field=models.CharField(max_length=100),
        ),
    ]
