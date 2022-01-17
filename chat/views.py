from email import message
from django.shortcuts import render
from chat.models import Message
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ChatSerializers
from rest_framework import status


# Create your views here.
# lấy tin nhắn
class GetMessage(APIView):
    def get(self, request):
        user = request.user.username
        message = Message.objects.filter(username=user)
        mychat = ChatSerializers(message, many=True)
        return Response(data=mychat.data, status=status.HTTP_200_OK)


class GetMessageAdmin(APIView):
    def post(self, request):
        user = request.data['username']
        message = Message.objects.filter(username=user)
        mychat = ChatSerializers(message, many=True)
        return Response(data=mychat.data, status=status.HTTP_200_OK)


# gửi tin nhắn
class SendMessage(APIView):
    def post(self, request):
        newMessage = ChatSerializers(data=request.data)
        if not newMessage.is_valid():
            return Response({"status": "Failed"}, status=status.HTTP_400_BAD_REQUEST)
        Message.objects.create(username=request.user.username,
                               chat=request.data['chat'],
                               checkUser=request.data['checkUser'])
        return Response({"status": "Successfully"}, status=status.HTTP_201_CREATED)


class SendMessageAdmin(APIView):
    def post(self, request):
        Message.objects.create(username=request.data['username'],
                               chat=request.data['chat'],
                               checkUser=request.data['checkUser'])
        return Response({"status": "Successfully"}, status=status.HTTP_201_CREATED)


# đếm số tin nhắn chưa đọc của người dùng
class GetCountUser(APIView):
    def get(self, request):
        user = request.user.username
        message = Message.objects.filter(username=user).filter(checkUser=True).filter(seen=False)
        count = message.count()
        return Response({"count": count}, status=status.HTTP_200_OK)


# đếm số tin nhắn chưa đọc của admin
class GetCountAdmin(APIView):
    def post(self,request):
        user = request.data['username']
        message = Message.objects.filter(username = user).filter(checkUser = False).filter(seen = False)
        count = message.count()
        return Response({"count":count},status=status.HTTP_200_OK)


# cập nhật trạng thái thành đã xem của tin nhắn
class UpdateSeen(APIView):
    def post(self, request):
        username = request.data['username']
        checkUser = request.data['checkUser']
        message = Message.objects.filter(username= username).filter(checkUser=checkUser).filter(seen=False)
        for i in message:
            i.seen = True
            i.save()
        return Response(data=None)
