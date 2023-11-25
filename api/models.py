from django.db import models


class AirPlane(models.Model):
    name = models.TextField(blank=False)
    photo = models.ImageField(blank=True, null=True)
    air_carrier = models.TextField(blank=False)
    fuel_capacity = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    cruise_speed = models.DecimalField(max_digits=6, decimal_places=2, blank=False)
    average_fuel_consumption = models.DecimalField(max_digits=5, decimal_places=2, blank=False)
    number_of_passengers = models.DecimalField(max_digits=4, decimal_places=0, blank=False)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class AirPort(models.Model):
    name = models.TextField(blank=False)
    photo = models.ImageField(blank=True, null=True)
    latitude = models.DecimalField(max_digits=6, decimal_places=4, blank=False)
    longitude = models.DecimalField(max_digits=7, decimal_places=4, blank=False)
    country = models.TextField(blank=False)
    currency = models.TextField(blank=False)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
