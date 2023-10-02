from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Thing(models.Model):
    name = models.CharField(max_length = 30, unique = True, blank = False)  # Adjust the max_length as needed
    description = models.CharField(max_length=120, unique = False, blank = True)  # Adjust the max_length as needed
    quantity = models.IntegerField(unique = False, validators = [
        MaxValueValidator(100),
        MinValueValidator(0)
    ] )
