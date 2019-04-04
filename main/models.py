from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
from datetime import datetime


class Car(models.Model):
    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'

    def __str__(self):
        return self.name

    name = models.CharField(max_length=30, verbose_name='Name')
    manufacturer = models.CharField(max_length=50, verbose_name='Manufacturer',
                                    null=True, blank=True)
    model = models.CharField(max_length=30, verbose_name='Model', null=True,
                             blank=True)
    issue_year = models.PositiveIntegerField(verbose_name='Year of issue',
                                             validators=[
                                                 MinValueValidator(1990)],
                                             null=True, blank=True)
    cost = models.FloatField(verbose_name='Cost',
                             validators=[MinValueValidator(0)], null=True,
                             blank=True)
    mileage = models.FloatField(verbose_name='Mileage',
                                validators=[MinValueValidator(0)], null=True,
                                blank=True)
    registration_number = models.CharField(max_length=7,
                                           verbose_name='Registration number',
                                           null=True, blank=True)
    fuel_type = models.CharField(verbose_name="fuel's type", max_length=30,
                                 null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             verbose_name='owner', related_name='cars')


class Note(models.Model):
    class Meta:
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'

    def __str__(self):
        return "Note"

    odometer = models.FloatField(verbose_name='Odometr')
    fuel_volume = models.FloatField(verbose_name="Fuel's volume",
                                    validators=[MinValueValidator(0)])
    cost = models.FloatField(verbose_name='Cost',
                             validators=[MinValueValidator(0)])
    date = models.DateTimeField(verbose_name='Время', default=datetime.now)
    fuel_type = models.CharField(verbose_name="Fuel's type", max_length=30)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name='Car',
                            related_name='notes')
