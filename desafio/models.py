from django.db import models

# Create your models here.
class Region (models.Model):
    name = models.CharField(max_length=20, primary_key=True)

class Fruit (models.Model):
    name = models.CharField(max_length=20)
    region_name = models.ForeignKey(Region,on_delete=models.CASCADE)