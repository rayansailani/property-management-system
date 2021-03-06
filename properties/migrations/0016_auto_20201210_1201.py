# Generated by Django 3.1.3 on 2020-12-10 06:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('properties', '0015_auto_20201126_2242'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appointment',
            options={'verbose_name': 'Appointment ', 'verbose_name_plural': 'Appointments for sale'},
        ),
        migrations.CreateModel(
            name='visit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_appointement', models.DateField()),
                ('time_appointment', models.TimeField()),
                ('owner', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='ppty_owner_rent', to=settings.AUTH_USER_MODEL)),
                ('property', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='properties.propertyforrent')),
                ('visitor', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Appointment ',
                'verbose_name_plural': 'Appointments for rent',
            },
        ),
    ]
