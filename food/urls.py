from django.urls import path
from .views import GetFood, CreateFood, DeleteFood, EditFood


urlpatterns = [
    path('getfood', GetFood.as_view(), name='get_food'),
    path('createfood', CreateFood.as_view(), name='create_food'),
    path('deletefood', DeleteFood.as_view(), name='delete_food'),
    path('editfood', EditFood.as_view(), name='edit_food'),
]
