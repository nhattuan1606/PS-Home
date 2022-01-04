from django.urls import path
from .views import GetNotification, CreateNotification, DeleteNotification, GetCount


urlpatterns = [
    path('getnotification', GetNotification.as_view(), name='get_noti'),
    path('createnotification', CreateNotification.as_view(), name='create_noti'),
    path('deletenotification', DeleteNotification.as_view(), name='delete_noti'),
    path('getcount', GetCount.as_view(), name='get_count'),
]
