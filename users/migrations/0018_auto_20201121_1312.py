# Generated by Django 3.1.3 on 2020-11-21 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_auto_20201121_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tenant',
            name='address_proof',
            field=models.ImageField(default='adress_proofs/default.jpg', upload_to='address_proofs/'),
        ),
    ]
