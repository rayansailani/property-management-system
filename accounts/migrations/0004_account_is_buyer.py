# Generated by Django 3.1.3 on 2021-01-07 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_account_is_tenant'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='is_buyer',
            field=models.BooleanField(default=True),
        ),
    ]
