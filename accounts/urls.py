from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

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
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
]