from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Statistical
from .serializer import Stat


# Create your views here.
class CreateStat(APIView):
    def post(self, request):
        Statistical.objects.create(priceFood=request.data['priceFood'], priceMoney=request.data['priceMonney'])
        return Response(data=None)


class GetStat(APIView):
    def get(self, request):
        priceFood = 0
        priceMonney = 0
        stat = Statistical.objects.all()
        for tmp in stat:
            priceFood += tmp.priceFood
            priceMonney += tmp.priceMoney
        return Response(data={"priceMonney": priceMonney,
                              "priceFood": priceFood,
                              "stat": Stat(stat, many=True).data})
