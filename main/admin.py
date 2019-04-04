from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Car, Note


class CarAdmin(ModelAdmin):
    list_display = ('name', 'manufacturer', 'model',
                    'issue_year', 'cost', 'registration_number', 'user')


class NoteAdmin(ModelAdmin):
    list_display = ('car', 'odometer', 'fuel_volume',
                    'cost', 'date', 'fuel_type')


admin.site.register(Car, CarAdmin)
admin.site.register(Note, NoteAdmin)
