from django.db import models

class Director(models.Model):
    name = models.CharField(max_length=50)
    link = models.CharField(max_length=200)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Location(models.Model):
    borough = models.CharField(max_length=100)
    neighborhood = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=20,decimal_places=17)
    longitude = models.DecimalField(max_digits=20,decimal_places=17)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Film(models.Model):
    title = models.CharField(max_length=50)
    link = models.CharField(max_length=50)
    year = models.CharField(max_length=20)
    director = models.ForeignKey(Director)
    location = models.ForeignKey(Location)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
