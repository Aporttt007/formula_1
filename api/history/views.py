from rest_framework import viewsets
from .models import HistoryAchievements
from .serializers import HistoryAchievementsSerializer

class HistoryAchievementsViewSet(viewsets.ModelViewSet):
    queryset = HistoryAchievements.objects.all()
    serializer_class = HistoryAchievementsSerializer
