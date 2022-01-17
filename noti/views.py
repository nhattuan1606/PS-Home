from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Noti, NotiUser
from rest_framework import status
from .serializers import NotiSerializer, NotiUserSerializer


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


class ReturnNotification(APIView):
    def post(self, request):
        noti = Noti.objects.get(id=request.data['id'])

        NotiUser.objects.create(username=noti.username, name=noti.name, approve=int(request.data['check']))
        noti.delete()
        return Response(data=None)


class GetCount(APIView):
    def get(self, request):
        return Response({"count": Noti.objects.all().count()}, status=status.HTTP_200_OK)


class GetCountUser(APIView):
    def get(self, request):
        count = NotiUser.objects.filter(username=request.user.username).filter(seen=False).count()
        return Response({"count": count}, status=status.HTTP_200_OK)


class GetNotificationUser(APIView):
    def get(self, request):
        noti = NotiUser.objects.filter(username=request.user.username).all()
        # noti.reverse()
        return Response(data=NotiUserSerializer(noti, many=True).data.__reversed__(), status=status.HTTP_200_OK)


class SeenNotification(APIView):
    def get(self, request):
        noti = NotiUser.objects.filter(username=request.user.username).all()
        for tmp in noti:
            tmp.seen = True
            tmp.save()
        return Response(data=None)


class DeleteNotification(APIView):
    def get(self, request):
        noti = NotiUser.objects.filter(username=request.user.username).filter(seen=True)
        for tmp in noti:
            tmp.delete()
        return Response(data=None)
