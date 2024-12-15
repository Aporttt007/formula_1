from rest_framework import serializers
from .models import User, Merchandise
from teams.models import Team, Driver
from teams.serializers import TeamSerializer, DriverSerializer

class UserSerializer(serializers.ModelSerializer):
    favorite_team = TeamSerializer(read_only=True)
    favorite_team_id = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all(), write_only=True, source='favorite_team')
    favorite_driver = DriverSerializer(read_only=True)
    favorite_driver_id = serializers.PrimaryKeyRelatedField(queryset=Driver.objects.all(), write_only=True, source='favorite_driver')

    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password', 'favorite_team', 'favorite_team_id', 'favorite_driver', 'favorite_driver_id']
        extra_kwargs = {
            'password': {'write_only': True}
        }

class MerchandiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merchandise
        fields = ['id', 'name', 'price', 'stock', 'category']
