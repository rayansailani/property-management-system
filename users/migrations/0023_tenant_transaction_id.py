# Generated by Django 3.1.3 on 2020-11-22 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0008_auto_20201122_1945'),
        ('users', '0022_auto_20201122_1238'),
    ]

    operations = [
        migrations.AddField(
            model_name='tenant',
            name='transaction_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='payments.rentpayment'),
        ),
    ]