from rest_framework import serializers
from .models import Ticket, MediaCoverage, LiveStream
from races.models import Race
from races.serializers import RaceSerializer

class TicketSerializer(serializers.ModelSerializer):
    race = RaceSerializer(read_only=True)
    race_id = serializers.PrimaryKeyRelatedField(queryset=Race.objects.all(), write_only=True, source='race')

    class Meta:
        model = Ticket
        fields = ['id', 'race', 'race_id', 'price', 'purchase_date', 'seat', 'type']

class MediaCoverageSerializer(serializers.ModelSerializer):
    race = RaceSerializer(read_only=True)
    race_id = serializers.PrimaryKeyRelatedField(queryset=Race.objects.all(), write_only=True, source='race')

    class Meta:
        model = MediaCoverage
        fields = ['id', 'race', 'race_id', 'broadcaster', 'platform', 'language']

class LiveStreamSerializer(serializers.ModelSerializer):
    race = RaceSerializer(read_only=True)
    race_id = serializers.PrimaryKeyRelatedField(queryset=Race.objects.all(), write_only=True, source='race')

    class Meta:
        model = LiveStream
        fields = ['id', 'race', 'race_id', 'platform', 'start_time', 'end_time']
