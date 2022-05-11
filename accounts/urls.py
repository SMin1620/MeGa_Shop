from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from accounts.views import UserCreateAPI, UserLoginAPI, RefreshTokenAPI
from accounts.views import MyTokenObtainPairView

app_name = 'account'

# 사용자 목록 - 테스트용
user_list = UserCreateAPI.as_view({
    'get': 'list'
})

register = UserCreateAPI.as_view({
    'post': 'create',
})


# login url
login_urlpatterns = [
    path('', UserLoginAPI.as_view(), name='login'),
    path('refresh/', RefreshTokenAPI.as_view(), name='refresh')
]


urlpatterns = [
    path('', user_list),
    path('signup/', register),
    path('login/', include(login_urlpatterns)),
    path('token/', TokenObtainPairView.as_view()),
    path('token/verify/', TokenVerifyView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
]