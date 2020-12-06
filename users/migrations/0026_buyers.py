# Generated by Django 3.1.3 on 2020-11-25 17:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0025_remove_tenant_transaction_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buyers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catagory', models.CharField(choices=[('Agent', 'Agent'), ('Buyer', 'Buyer')], default=2, max_length=20)),
                ('name', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
