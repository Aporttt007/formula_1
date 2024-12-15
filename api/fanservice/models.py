from django.db import models
from teams.models import Team, Driver

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    favorite_team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True, related_name='fans')
    favorite_driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True, blank=True, related_name='fans')

    def __str__(self):
        return self.name

class Merchandise(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.name
