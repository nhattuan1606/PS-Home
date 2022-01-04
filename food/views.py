from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import FoodSerializer
from .models import Food


# Create your views here.
class GetFood(APIView):
    def get(self, request):
        list_food = Food.objects.all()
        return Response(data=FoodSerializer(list_food, many=True).data, status=status.HTTP_200_OK)


class CreateFood(APIView):
    def post(self, request):
        new_food = FoodSerializer(data=request.data)
        if not new_food.is_valid():
            return Response({"Status": "Wrong data"}, status=status.HTTP_400_BAD_REQUEST)

        if Food.objects.filter(name=new_food.data['name']).exists():
            return Response({"Status": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST)

        Food.objects.create(name=new_food.data['name'], url=new_food.data['url'], price=new_food.data['price'])
        return Response({"Status": "Created"}, status=status.HTTP_201_CREATED)


class DeleteFood(APIView):
    def post(self, request):
        Food.objects.get(name=request.data['name']).delete()
        return Response(data=None)


class EditFood(APIView):
    def post(self, request):
        food = Food.objects.get(name=request.data['nameold'])
        food.name = request.data['name']
        food.url = request.data['url']
        food.price = request.data['price']
        food.save()
        return Response(data=None)
