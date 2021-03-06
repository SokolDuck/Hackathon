# Generated by Django 2.2 on 2019-04-03 15:40

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('manufacturer', models.CharField(max_length=50, verbose_name='Manufacter')),
                ('model', models.CharField(max_length=30, verbose_name='Model')),
                ('issue_year', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1990)], verbose_name='Year of issue')),
                ('cost', models.FloatField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Cost')),
                ('mileage', models.FloatField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Mileage')),
                ('registration_number', models.PositiveIntegerField(verbose_name='Registration number')),
                ('fuel_type', models.CharField(max_length=30, verbose_name="fuel's type")),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to=settings.AUTH_USER_MODEL, verbose_name='owner')),
            ],
            options={
                'verbose_name': 'Car',
                'verbose_name_plural': 'Cars',
            },
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('odometer', models.FloatField(verbose_name='Odometr')),
                ('fuel_volume', models.FloatField(validators=[django.core.validators.MinValueValidator(0)], verbose_name="Fuel's volume")),
                ('cost', models.FloatField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Cost')),
                ('fuel_type', models.CharField(max_length=30, verbose_name="Fuel's type")),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='main.Car', verbose_name='Car')),
            ],
            options={
                'verbose_name': 'Note',
                'verbose_name_plural': 'Notes',
            },
        ),
    ]
