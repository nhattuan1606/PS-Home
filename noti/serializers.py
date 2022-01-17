from rest_framework import serializers
from .models import Noti, NotiUser


class NotiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Noti
        fields = ('id', 'username', 'name', 'notification', 'quantity', 'price')


class NotiUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotiUser
        fields = ('id', 'name', 'approve', 'seen')
