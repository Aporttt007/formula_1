from django.db import models
from races.models import Race

class Ticket(models.Model):
    race = models.ForeignKey(Race, on_delete=models.CASCADE, related_name='tickets')
    price = models.FloatField()
    purchase_date = models.DateField()
    seat = models.CharField(max_length=255)
    type = models.CharField(max_length=255)

    def __str__(self):
        return f"Ticket for {self.race.name} - {self.seat}"

class MediaCoverage(models.Model):
    race = models.ForeignKey(Race, on_delete=models.CASCADE, related_name='media_coverages')
    broadcaster = models.CharField(max_length=255)
    platform = models.CharField(max_length=255)
    language = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.broadcaster} on {self.platform} - {self.race.name}"

class LiveStream(models.Model):
    race = models.ForeignKey(Race, on_delete=models.CASCADE, related_name='live_streams')
    platform = models.CharField(max_length=255)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"Stream of {self.race.name} on {self.platform}"
