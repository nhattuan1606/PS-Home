from .models import Statistical
from rest_framework import serializers


class Stat(serializers.ModelSerializer):
    class Meta:
        model = Statistical
        fields = ('priceFood', 'priceMoney', 'date')
