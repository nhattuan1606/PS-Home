from django.db import models


# Create your models here.
class Statistical(models.Model):
    priceFood = models.IntegerField(blank=True, null=True)
    priceMoney = models.IntegerField(blank=True, null=True)
    date = models.DateField()
