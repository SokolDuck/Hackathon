# Generated by Django 2.2 on 2019-04-04 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20190403_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='registration_number',
            field=models.CharField(blank=True, max_length=7, null=True, verbose_name='Registration number'),
        ),
    ]
