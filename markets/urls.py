from django.urls import path, include
from rest_framework.routers import DefaultRouter

from markets.views import MarketListAPI


app_name = 'markets'

router = DefaultRouter()
router.register('', MarketListAPI)


urlpatterns = [
    path('', include(router.urls)),
]
