from datetime import datetime
from email import message
from pickle import TRUE
from django.db import models

# Create your models here.
class Room(models.Model):
    name=models.CharField(max_length=1000000)

    def __str__(self):
        return self.name

class Message(models.Model):
    value=models.CharField(max_length=1000000)
    time=models.CharField(default=datetime.now(),blank=True,max_length=1000000)
    user=models.CharField(max_length=1000000)
    room=models.CharField(max_length=1000000)
    
    def __str__(self):
        return self.user