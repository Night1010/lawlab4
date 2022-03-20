from django.db import models
from django.core.validators import  MinValueValidator

# Create your models here.
class Adventurer(models.Model):
    name = models.CharField(max_length=255)
    job = models.CharField(max_length=255)
    race = models.CharField(max_length=255)
    level = models.IntegerField(validators=[MinValueValidator(1)])


    def __str__(self):
        return self.name

class Image(models.Model):
    image = models.ImageField()