from django.db import models

class Coordinate(models.Model):
    latitude = models.DecimalField(max_digits=20,decimal_places=17)
    longitude = models.DecimalField(max_digits=20,decimal_places=17)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Location(models.Model):
    borough = models.CharField(max_length=100)
    neighborhood = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    coordinate = models.ManyToManyField(Coordinate)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Link(models.Model):
    link = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Director(models.Model):
    name = models.CharField(max_length=100)
    link = models.ForeignKey(Link)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Film(models.Model):
    title = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    link = models.ForeignKey(Link)
    director = models.ManyToManyField(Director)
    location = models.ManyToManyField(Location)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
