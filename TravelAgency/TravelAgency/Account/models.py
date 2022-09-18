from django.db import models

# Create your models here.


class Profile(models.Model):
    gender = [
        ('Man','Man'),
        ('Woman', 'Woman'),
        ('NoGender', 'NoGender'),
    ]
    # image = models.ImageField(null=True,blank=True)
    name = models.CharField(max_length=100)
    family = models.CharField(max_length=100)
    id_code = models.IntegerField(null=True,blank=True)
    email = models.EmailField()
    phone = models.IntegerField(null=True,blank=True)
    gender = models.CharField(null=True,blank=True,choices=gender,max_length=10)
    birth_date = models.CharField(null=True,blank=True,max_length=10)
