from django.urls import path, include
from rest_framework.routers import DefaultRouter

from products.views import ProductListAPI


app_name = 'products'

router = DefaultRouter()
router.register('', ProductListAPI)


urlpatterns = [
    path('', include(router.urls)),
]
