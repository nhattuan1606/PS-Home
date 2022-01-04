from django.db import models


# Create your models here.
class InforUser(models.Model):
    username = models.CharField(max_length=30, primary_key=True)
    password = models.CharField(max_length=30)
    time = models.DateTimeField(default=None, null=True, blank=True)
    monney = models.FloatField(default=0)
    is_locked = models.BooleanField(default=False)
    note = models.TextField(max_length=300, null=True, blank=True)
