from pyexpat import model
from django.db import models

# Create your models here.
class ParkingSpace(models.Model):
    Name = models.CharField(max_length=200)

def __str__(self):
    return self.name

class Car(models.Model):
    ParkingSpace = models.ForeignKey(ParkingSpace, on_delete=models.CASCADE)
    carName = models.CharField(max_length=200)
    plateNumber = models.CharField(max_length=200)
    parked = models.BooleanField()
    
def __str__(self):
    return self.carName




