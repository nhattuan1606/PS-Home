from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import InforUser
from rest_framework import status
from .serializers import InforUserSerializer, RegisterSerializer, NewPassword, CustomTokenObtainPairSerializer
from django.contrib.auth.models import User


# Create your views here.
class CustomTokenObtainPairView(TokenObtainPairView):

    serializer_class = CustomTokenObtainPairSerializer


class GetUser(APIView):
    def get(self, request):
        curr_user = InforUser.objects.get(username=request.user.username)
        return Response({
            "username": curr_user.username,
            "monney": curr_user.monney
        }, status=status.HTTP_200_OK)


class RegisterAcc(APIView):
    def post(self, request):
        new_acc = RegisterSerializer(data=request.data)
        if not new_acc.is_valid():
            return Response({"Status": "Wrong data"}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=request.data['username']).exists():
            return Response({"Status": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST)

        User.objects.create_user(username=request.data['username'], password=request.data['password'])

        InforUser.objects.create(username=request.data['username'],
                                 password=request.data['password'],
                                 monney=request.data['monney'])
        return Response({"Status": "Created"}, status=status.HTTP_201_CREATED)


class ChangePassword(APIView):
    def post(self, request):
        user = User.objects.get(username=request.user.username)
        if not user.check_password(request.data['oldpassword']):
            return Response({"status": 0}, status=status.HTTP_200_OK)

        new_pass = NewPassword(data=request.data)
        if not new_pass.is_valid():
            return Response({"status": "Wrong data"}, status=status.HTTP_400_BAD_REQUEST)

        # Thay dổi ở bảng auth_user sẵn có của django
        user.set_password(new_pass.data['newpassword'])
        user.save()

        # Thay đổi ở bảng InforUser
        user = InforUser.objects.get(username=request.user.username)
        user.password = new_pass.data['newpassword']
        user.save()

        return Response({"Status": "Complete"}, status=status.HTTP_200_OK)


class MoreMonney(APIView):
    def post(self, request):
        acc = InforUser.objects.get(username=request.user.username)
        acc.monney = int(request.data['moremonney'])
        acc.save()
        return Response(data=None, status=status.HTTP_200_OK)


class GetAllUser(APIView):
    def get(self, request):
        all_user = InforUser.objects.all().exclude(username="admin")
        return Response(data=InforUserSerializer(all_user, many=True).data, status=status.HTTP_200_OK)


class DeleteUser(APIView):
    def post(self, request):
        User.objects.get(username=request.data['username']).delete()

        InforUser.objects.get(username=request.data['username']).delete()
        return Response(data=None)


class MoreMoneyUser(APIView):
    def post(self, request):
        user = InforUser.objects.get(username=request.data['username'])
        user.monney = int(request.data['moremonney'])
        user.save()
        return Response({"Status": "Complete"}, status=status.HTTP_200_OK)


class LockUser(APIView):
    def post(self, request):
        user = InforUser.objects.get(username=request.data['username'])
        user.is_locked = not user.is_locked
        user.save()
        return Response(data=None)
