from unittest.util import _MAX_LENGTH
from django.db import models

class Drink(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name + '' + self.description
