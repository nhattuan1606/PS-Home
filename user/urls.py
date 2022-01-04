from django.urls import path
from .views import CustomTokenObtainPairView, GetUser, ChangePassword, MoreMonney, GetAllUser, RegisterAcc, \
    DeleteUser, MoreMoneyUser


urlpatterns = [
    path('login', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('getuser', GetUser.as_view(), name='get_user'),
    path('changepassword', ChangePassword.as_view(), name='change_password'),
    path('moremonney', MoreMonney.as_view(), name='more_money'),
    path('getalluser', GetAllUser.as_view(), name='get_all_user'),
    path('createuser', RegisterAcc.as_view(), name='create_user'),
    path('deleteuser', DeleteUser.as_view(), name='delete_user'),
    path('moremonneyuser', MoreMoneyUser.as_view(), name='more_money_user'),
]
