from django.db import models

# Create your models here.
class Car(models.Model):
    car_name = models.CharField(max_length=200)
