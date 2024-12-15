from django.contrib import admin
from .models import Circuit

@admin.register(Circuit)
class CircuitAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'length_km', 'turns', 'lap_record')
    search_fields = ('name', 'country')
