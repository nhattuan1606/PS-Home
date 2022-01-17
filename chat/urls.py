from django.urls import path
from . import views 
from .views import GetCountAdmin, GetCountUser, GetMessage,SendMessage, UpdateSeen
urlpatterns = [
    path('viewchat',GetMessage.as_view()),
    path('sendmessage',SendMessage.as_view()),
    path('countUserMessage',GetCountUser.as_view()),
    path('countAdminMessage',GetCountAdmin.as_view()),
    path('updateSeen',UpdateSeen.as_view())
]
