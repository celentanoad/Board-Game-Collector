from django.db import models
from django.urls import reverse

# Create your models here.

class Game(models.Model):
    name = models.CharField(max_length=250)
    numPlayers = models.IntegerField('Number of Players')
    description = models.TextField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'game_id': self.id})

class Store(models.Model):
    name = models.CharField(max_length=250)
    location = models.CharField(max_length=400)

    def __str__(self):
        return self.name