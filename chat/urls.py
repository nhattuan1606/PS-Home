from django.urls import path
from .views import GetCountAdmin, GetCountUser, GetMessage,SendMessage, UpdateSeen, GetMessageAdmin, SendMessageAdmin
urlpatterns = [
    path('viewchat', GetMessage.as_view()),
    path('sendmessage', SendMessage.as_view()),
    path('countusermessage', GetCountUser.as_view()),
    path('countadminmessage', GetCountAdmin.as_view()),
    path('updateseen', UpdateSeen.as_view()),
    path('viewchatadmin', GetMessageAdmin.as_view()),
    path('sendmessadmin', SendMessageAdmin.as_view()),
]
