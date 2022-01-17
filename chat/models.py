from datetime import datetime
from django.db import models


# Create your models here.
class Message(models.Model):
    username = models.CharField(max_length=30, null=True, blank=True)
    chat = models.TextField(max_length=3000)
    seen = models.BooleanField(default=False)
    date = models.DateTimeField(default=datetime.now, blank=True)
    checkUser = models.BooleanField(default=True)
