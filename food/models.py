from django.db import models


# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=30)
    url = models.TextField(max_length=300)
    price = models.IntegerField()
