# Generated by Django 3.1.3 on 2020-11-21 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20201120_2135'),
    ]

    operations = [
        migrations.AddField(
            model_name='tenant',
            name='address_proof',
            field=models.ImageField(default=None, upload_to='address_proofs/'),
        ),
    ]