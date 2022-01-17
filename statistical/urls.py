from django.urls import path
from .views import CreateStat, GetStat


urlpatterns = [
    path('createstatistical', CreateStat.as_view()),
    path('getStatiscical', GetStat.as_view())
]
