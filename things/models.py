from django.db import models
# Create your models here.

class Thing(models.Model):
    name = models.CharField(max_length=255)  # Adjust the max_length as needed
    description = models.CharField(max_length=255)  # Adjust the max_length as needed
    quantity = models.IntegerField()
