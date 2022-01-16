from django.urls import path
from .views import GetNotification, CreateNotification, ReturnNotification, GetCount


urlpatterns = [
    path('getnotification', GetNotification.as_view(), name='get_noti'),
    path('createnotification', CreateNotification.as_view(), name='create_noti'),
    path('returnnotification', ReturnNotification.as_view(), name='return_noti'),
    path('getcount', GetCount.as_view(), name='get_count'),
]
