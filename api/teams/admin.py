from django.contrib import admin
from .models import Sponsor, Team, Driver, Car

@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'contact_info', 'contract_duration')
    search_fields = ('name', 'category')

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'team_leader', 'sponsor')
    search_fields = ('name', 'country', 'team_leader')
    list_filter = ('country', 'sponsor')

@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'nationality', 'team', 'points', 'championships')
    search_fields = ('name', 'nationality', 'team__name')
    list_filter = ('nationality', 'team')

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'team', 'driver', 'engine', 'chassis', 'weight', 'tyre_type')
    search_fields = ('team__name', 'driver__name', 'engine', 'chassis')
    list_filter = ('team', 'tyre_type')
