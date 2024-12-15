from django.db import models

class Circuit(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    length_km = models.FloatField()
    turns = models.IntegerField()
    lap_record = models.CharField(max_length=255)

    def __str__(self):
        return self.name
