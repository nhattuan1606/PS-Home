from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Noti
from rest_framework import status
from .serializers import NotiSerializer


# Create your views here.
class GetNotification(APIView):
    def get(self, request):
        noti = Noti.objects.all()
        return Response(data=NotiSerializer(noti, many=True).data, status=status.HTTP_200_OK)


class CreateNotification(APIView):
    def post(self, request):
        Noti.objects.create(username=request.data['username'],
                            name=request.data['name'],
                            notification=request.data['notification'],
                            quantity=request.data['quantity'],
                            price=request.data['price'])
        return Response(data=None)


class DeleteNotification(APIView):
    def post(self, request):
        Noti.objects.get(id=request.data['id']).delete()
        return Response(data=None)
        # noti = Noti.objects.get(id=request.data['id'])
        # return Response(data=NotiSerializer(noti).data, status=status.HTTP_200_OK)


class GetCount(APIView):
    def get(self, request):
        return Response({"count": Noti.objects.all().count()}, status=status.HTTP_200_OK)
