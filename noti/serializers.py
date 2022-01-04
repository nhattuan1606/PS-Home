from rest_framework import serializers
from .models import Noti


class NotiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Noti
        fields = ('id', 'username', 'name', 'notification', 'quantity', 'price')
