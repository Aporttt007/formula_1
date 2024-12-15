from django.contrib import admin
from .models import Race, RaceResult, PitStop, SessionTiming

@admin.register(Race)
class RaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'date', 'laps', 'race_type', 'circuit')
    search_fields = ('name', 'location', 'race_type', 'circuit__name')
    list_filter = ('location', 'race_type', 'circuit')

@admin.register(RaceResult)
class RaceResultAdmin(admin.ModelAdmin):
    list_display = ('race', 'driver', 'position', 'points', 'fastest_lap')
    search_fields = ('race__name', 'driver__name')
    list_filter = ('race', 'fastest_lap')

@admin.register(PitStop)
class PitStopAdmin(admin.ModelAdmin):
    list_display = ('race', 'driver', 'lap_number', 'duration', 'reason')
    search_fields = ('race__name', 'driver__name', 'reason')
    list_filter = ('race',)

@admin.register(SessionTiming)
class SessionTimingAdmin(admin.ModelAdmin):
    list_display = ('race', 'driver', 'session_type', 'lap_time', 'position')
    search_fields = ('race__name', 'driver__name', 'session_type')
    list_filter = ('session_type', 'race')
