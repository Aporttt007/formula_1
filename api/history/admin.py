from django.contrib import admin
from .models import HistoryAchievements

@admin.register(HistoryAchievements)
class HistoryAchievementsAdmin(admin.ModelAdmin):
    list_display = ('driver', 'team', 'season', 'achievement', 'record_type', 'year')
    search_fields = ('driver__name', 'team__name', 'achievement', 'record_type')
    list_filter = ('season', 'year', 'team', 'driver')
