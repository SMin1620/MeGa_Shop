from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedSimpleRouter

from products.views import ProductReadAPI


app_name = 'products'

# 상품 리스트 url
product_list = ProductReadAPI.as_view({
    'get': 'list'
})

# 상품 디테일 url
product_detail = ProductReadAPI.as_view({
    'get': 'retrieve'
})


urlpatterns = [
    path('', product_list),
    path('<int:product_id>/', product_detail),
]
