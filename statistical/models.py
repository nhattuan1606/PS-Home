from django.db import models
from datetime import date, datetime


# Create your models here.
class Statistical(models.Model):
    priceFood = models.IntegerField(blank=True, null=True)
    priceMoney = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(default=datetime.now())
