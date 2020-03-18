from django.db import models
from django.urls import reverse

# Create your models here.

class Store(models.Model):
    name = models.CharField(max_length=250)
    location = models.CharField(max_length=400)

    def __str__(self):
        return self.name
        
class Game(models.Model):
    name = models.CharField(max_length=250)
    numPlayers = models.IntegerField('Number of Players')
    description = models.TextField()
    stores = models.ManyToManyField(Store)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'game_id': self.id})

class Photo(models.Model):
    url = models.CharField(max_length=2000)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for game_id: {self.game_id} @{self.url}"