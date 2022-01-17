from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import InforUser


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super(CustomTokenObtainPairSerializer, self).validate(attrs)
        current_user = InforUser.objects.get(username=self.user.username)
        if current_user.is_locked:
            return {"status": "lock"}
        data.update({"monney": current_user.monney, "status": "ok"})
        return data


class InforUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = InforUser
        fields = ('username', 'password', 'time', 'monney', 'is_locked', 'note')


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=30)
    password = serializers.CharField(max_length=30)
    monney = serializers.FloatField()


class NewPassword(serializers.Serializer):
    newpassword = serializers.CharField(max_length=30)
