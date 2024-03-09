from django.db import models

# Create your models here.

class Car(models.Model):
    brandname = models.CharField(max_length=50)
    modelname = models.CharField(max_length=100)
    year = models.IntegerField()