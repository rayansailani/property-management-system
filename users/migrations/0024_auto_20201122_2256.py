# Generated by Django 3.1.3 on 2020-11-22 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0008_auto_20201122_1945'),
        ('users', '0023_tenant_transaction_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tenant',
            name='transaction_id',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='payments.rentpayment'),
        ),
    ]
