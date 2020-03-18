from django.db import models

# Create your models here.

class Game(models.Model):
    name = models.CharField(max_length=250)
    publisher = models.CharField(max_length=250)
    numPlayers = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name
    
