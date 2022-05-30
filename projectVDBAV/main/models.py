from turtle import update
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    Owner = models.ForeignKey(User, on_delete=models.CASCADE)
    Carname = models.CharField(max_length=200)
    Carcolor = models.CharField(max_length=200)
    Platenumber = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.Carname + "\n" + self.Carcolor

class TimeIn_Out(models.Model):
    Parker = models.ForeignKey(User, on_delete=models.CASCADE)
    ParkerName =  models.CharField(max_length=200,blank=True, null=True)
    TimeIn = models.DateTimeField(auto_now_add=True)
    TimeOut = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return self.ParkerName 
   

    