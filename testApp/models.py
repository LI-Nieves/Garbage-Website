from django.db import models

# Create your models here.

class Character(models.Model):
    name = models.CharField(max_length = 10)
    level = models.IntegerField('Level')