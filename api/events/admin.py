from django.contrib import admin
from .models import Ticket, MediaCoverage, LiveStream

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('race', 'price', 'purchase_date', 'seat', 'type')
    search_fields = ('race__name', 'seat', 'type')
    list_filter = ('race', 'type', 'purchase_date')

@admin.register(MediaCoverage)
class MediaCoverageAdmin(admin.ModelAdmin):
    list_display = ('race', 'broadcaster', 'platform', 'language')
    search_fields = ('race__name', 'broadcaster', 'platform', 'language')
    list_filter = ('race', 'language', 'platform')

@admin.register(LiveStream)
class LiveStreamAdmin(admin.ModelAdmin):
    list_display = ('race', 'platform', 'start_time', 'end_time')
    search_fields = ('race__name', 'platform')
    list_filter = ('platform', 'race')
