from django.urls import path, include
from rest_framework.routers import DefaultRouter

from accounts.views import UserListAPI

app_name = 'account'


UserListViewSet = UserListAPI.as_view(
    {
        'get': 'list'
    }
)


urlpatterns = [
    path('', UserListViewSet, name='user_list'),
]