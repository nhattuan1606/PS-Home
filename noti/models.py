from django.db import models


# Create your models here.
class Noti(models.Model):
    username = models.CharField(max_length=30, null=True, blank=True)
    name = models.CharField(max_length=30, null=True, blank=True)
    notification = models.CharField(max_length=30, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    approve = models.IntegerField(default=0)
