from django.db import models

class Sponsor(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=255)
    contract_duration = models.DateField()

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    team_leader = models.CharField(max_length=255)
    sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE, related_name='teams')

    def __str__(self):
        return self.name

class Driver(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    nationality = models.CharField(max_length=255)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='drivers')
    points = models.IntegerField(default=0)
    championships = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Car(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='cars')
    driver = models.OneToOneField(Driver, on_delete=models.CASCADE, related_name='car')
    engine = models.CharField(max_length=255)
    chassis = models.CharField(max_length=255)
    weight = models.IntegerField()
    tyre_type = models.CharField(max_length=255)

    def __str__(self):
        return f"Car of {self.driver.name}"
