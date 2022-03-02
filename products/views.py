from django.shortcuts import render
from rest_framework import viewsets, mixins

from products.models import Product
from products.serializers import ProductSerializer


# Create your views here.
# 상품리스트 - 일반 사용자용
class ProductListAPI(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
