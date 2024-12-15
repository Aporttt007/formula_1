from django.db import models
from teams.models import Driver, Team

class HistoryAchievements(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='historical_achievements')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='historical_achievements')
    season = models.CharField(max_length=255)
    achievement = models.CharField(max_length=255)
    record_type = models.CharField(max_length=255)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.achievement} ({self.year})"
