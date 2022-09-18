from django.db import models

# Create your models here.


class Tour(models.Model):
    tour_name = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    date_start = models.DateTimeField(auto_now_add=True)
    date_end = models.DateTimeField(auto_now_add=True)
    traveler_adult = models.PositiveIntegerField(blank=True,null=True)
    traveler_child = models.PositiveIntegerField(blank=True,null=True)
    price = models.PositiveIntegerField()
    discount = models.PositiveIntegerField()
    total_price = models.IntegerField()
    description = models.TextField()