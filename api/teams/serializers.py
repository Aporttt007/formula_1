from rest_framework import serializers
from .models import Sponsor, Team, Driver, Car

class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = ['id', 'name', 'category', 'contact_info', 'contract_duration']

class TeamSerializer(serializers.ModelSerializer):
    # Если нужно, можно вложить сериализатор для Sponsor
    sponsor = SponsorSerializer(read_only=True)
    sponsor_id = serializers.PrimaryKeyRelatedField(queryset=Sponsor.objects.all(), write_only=True, source='sponsor')
    
    class Meta:
        model = Team
        fields = ['id', 'name', 'country', 'team_leader', 'sponsor', 'sponsor_id']

class DriverSerializer(serializers.ModelSerializer):
    # Можно показать имя команды, используя сериализатор или поле `team_id`
    team = TeamSerializer(read_only=True)
    team_id = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all(), write_only=True, source='team')
    
    class Meta:
        model = Driver
        fields = ['id', 'name', 'age', 'nationality', 'team', 'team_id', 'points', 'championships']

class CarSerializer(serializers.ModelSerializer):
    team = TeamSerializer(read_only=True)
    team_id = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all(), write_only=True, source='team')
    driver = DriverSerializer(read_only=True)
    driver_id = serializers.PrimaryKeyRelatedField(queryset=Driver.objects.all(), write_only=True, source='driver')

    class Meta:
        model = Car
        fields = ['id', 'team', 'team_id', 'driver', 'driver_id', 'engine', 'chassis', 'weight', 'tyre_type']
