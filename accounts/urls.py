from django.urls import path, include
from rest_framework.routers import DefaultRouter

from accounts.views import UserListAPI
from accounts.views import UserListAPI, UserCreateAPI

app_name = 'account'

# 사용자 목록 - 테스트용
user_list = UserCreateAPI.as_view({
    'get': 'list'
})

register = UserCreateAPI.as_view({
    'post': 'create',
})


urlpatterns = [
    path('', user_list),
    path('signup/', register),
]