from django.db import models
from circuits.models import Circuit
from teams.models import Driver

class Race(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    date = models.DateField()
    laps = models.IntegerField()
    race_type = models.CharField(max_length=255)
    circuit = models.ForeignKey(Circuit, on_delete=models.CASCADE, related_name='races', null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.date})"

class RaceResult(models.Model):
    race = models.ForeignKey(Race, on_delete=models.CASCADE, related_name='results')
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='race_results')
    position = models.IntegerField()
    points = models.IntegerField()
    fastest_lap = models.BooleanField(default=False)

    def __str__(self):
        return f"Result: {self.driver.name} in {self.race.name}"

class PitStop(models.Model):
    race = models.ForeignKey(Race, on_delete=models.CASCADE, related_name='pit_stops')
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='pit_stops')
    lap_number = models.IntegerField()
    duration = models.CharField(max_length=255)
    reason = models.CharField(max_length=255)

    def __str__(self):
        return f"PitStop {self.lap_number} {self.driver.name} at {self.race.name}"

class SessionTiming(models.Model):
    race = models.ForeignKey(Race, on_delete=models.CASCADE, related_name='session_timings')
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='session_timings')
    session_type = models.CharField(max_length=255)
    lap_time = models.TimeField()
    position = models.IntegerField()

    def __str__(self):
        return f"{self.session_type} - {self.driver.name} - {self.race.name}"
