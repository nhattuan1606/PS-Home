
from rest_framework import serializers
from .models import Message
from datetime import datetime


class ChatSerializers(serializers.ModelSerializer):
    class Meta :
        model = Message
        fields = ('id','username','chat','seen','date','checkUser')

