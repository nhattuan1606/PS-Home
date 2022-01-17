from django.urls import path
from .views import GetNotification, CreateNotification, ReturnNotification, GetCount, \
    GetCountUser, GetNotificationUser, SeenNotification, DeleteNotification


urlpatterns = [
    path('getnotification', GetNotification.as_view(), name='get_noti'),
    path('createnotification', CreateNotification.as_view(), name='create_noti'),
    path('returnnotification', ReturnNotification.as_view(), name='return_noti'),
    path('getcount', GetCount.as_view(), name='get_count'),
    path('getcountuser', GetCountUser.as_view(), name='get_count_user'),
    path('getnotiuser', GetNotificationUser.as_view(), name='get_notification_user'),
    path('seennotification', SeenNotification.as_view(), name='seen_notification'),
    path('deletenotification', DeleteNotification.as_view(), name='delete_notification'),
]
