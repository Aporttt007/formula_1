from rest_framework import serializers
from .models import Race, RaceResult, PitStop, SessionTiming
from circuits.models import Circuit
from teams.models import Driver
from circuits.serializers import CircuitSerializer
from teams.serializers import DriverSerializer

class RaceSerializer(serializers.ModelSerializer):
    circuit = CircuitSerializer(read_only=True)
    circuit_id = serializers.PrimaryKeyRelatedField(queryset=Circuit.objects.all(), write_only=True, source='circuit')
    
    class Meta:
        model = Race
        fields = ['id', 'name', 'location', 'date', 'laps', 'race_type', 'circuit', 'circuit_id']

class RaceResultSerializer(serializers.ModelSerializer):
    race = RaceSerializer(read_only=True)
    race_id = serializers.PrimaryKeyRelatedField(queryset=Race.objects.all(), write_only=True, source='race')
    driver = DriverSerializer(read_only=True)
    driver_id = serializers.PrimaryKeyRelatedField(queryset=Driver.objects.all(), write_only=True, source='driver')

    class Meta:
        model = RaceResult
        fields = ['id', 'race', 'race_id', 'driver', 'driver_id', 'position', 'points', 'fastest_lap']

class PitStopSerializer(serializers.ModelSerializer):
    race = RaceSerializer(read_only=True)
    race_id = serializers.PrimaryKeyRelatedField(queryset=Race.objects.all(), write_only=True, source='race')
    driver = DriverSerializer(read_only=True)
    driver_id = serializers.PrimaryKeyRelatedField(queryset=Driver.objects.all(), write_only=True, source='driver')

    class Meta:
        model = PitStop
        fields = ['id', 'race', 'race_id', 'driver', 'driver_id', 'lap_number', 'duration', 'reason']

class SessionTimingSerializer(serializers.ModelSerializer):
    race = RaceSerializer(read_only=True)
    race_id = serializers.PrimaryKeyRelatedField(queryset=Race.objects.all(), write_only=True, source='race')
    driver = DriverSerializer(read_only=True)
    driver_id = serializers.PrimaryKeyRelatedField(queryset=Driver.objects.all(), write_only=True, source='driver')

    class Meta:
        model = SessionTiming
        fields = ['id', 'race', 'race_id', 'driver', 'driver_id', 'session_type', 'lap_time', 'position']
