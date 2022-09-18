from django.db import models

# Create your models here.


class Ticket(models.Model):
    cobin_class = [
        ('FirstClass', 'FirstClass'),
        ('SecondClass', 'SecondClass'),
        ('ThirdClass', 'ThirdClass'),
    ]
    name_airline = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    hours = models.DateTimeField(auto_now_add=True)
    passenger_adult = models.PositiveIntegerField(blank=True,null=True)
    passenger_child = models.PositiveIntegerField(blank=True,null=True)
    cobin_class = models.CharField(null=True,blank=True,choices=cobin_class,max_length=15)
    price = models.PositiveIntegerField()
    discount = models.PositiveIntegerField()
    total_price = models.IntegerField()
