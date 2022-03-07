from django.urls import path, include
from rest_framework.routers import DefaultRouter

from accounts.views import UserListAPI
from accounts.views import UserListAPI

app_name = 'account'

router = DefaultRouter()

router.register(r'', UserListAPI)


urlpatterns = [
    path('', include(router.urls)),
]