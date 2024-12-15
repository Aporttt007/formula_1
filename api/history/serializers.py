from rest_framework import serializers
from .models import HistoryAchievements
from teams.serializers import TeamSerializer, DriverSerializer
from teams.models import Team, Driver

class HistoryAchievementsSerializer(serializers.ModelSerializer):
    driver = DriverSerializer(read_only=True)
    driver_id = serializers.PrimaryKeyRelatedField(queryset=Driver.objects.all(), write_only=True, source='driver')
    team = TeamSerializer(read_only=True)
    team_id = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all(), write_only=True, source='team')

    class Meta:
        model = HistoryAchievements
        fields = ['id', 'driver', 'driver_id', 'team', 'team_id', 'season', 'achievement', 'record_type', 'year']
