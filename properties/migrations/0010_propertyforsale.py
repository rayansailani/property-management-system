# Generated by Django 3.1.3 on 2020-11-24 11:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('properties', '0009_auto_20201121_1831'),
    ]

    operations = [
        migrations.CreateModel(
            name='PropertyForSale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.IntegerField()),
                ('locality', models.CharField(max_length=50)),
                ('area', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('width', models.IntegerField()),
                ('length', models.IntegerField()),
                ('cost_sqft', models.IntegerField()),
                ('ceritification', models.CharField(choices=[('A-Khata', 'A'), ('B-Khata', 'B')], default='B-Khata', max_length=8)),
                ('owner', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
