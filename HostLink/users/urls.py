from django.urls import path, include

from users.views import CreateUserAPI, LookUserApi
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView , TokenVerifyView

urlpatterns = [
    path('register/',CreateUserAPI.as_view() , name='register' ),
    path('login/', TokenObtainPairView.as_view() , name = 'login' ),
    path('authme/', LookUserApi.as_view(), name = 'look')


]
