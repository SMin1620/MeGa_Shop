from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from products.models import Product, ProductReal
from products.serializers import ProductSerializer, ProductRealSerializer
from base.drf.paginations import LargeResultsSetPagination


# Create your views here.
# 상품 리스트 - 일반 사용자용
class ProductReadAPI(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = LargeResultsSetPagination
    lookup_url_kwarg = 'product_id'

    def get_queryset(self):
        if self.action == 'list':
            queryset = Product.objects.all().select_related('category', 'market')
            return queryset

        if self.action == 'retrieve':
            queryset = Product.objects.all()
            return queryset


class ProductRealReadAPI(mixins.RetrieveModelMixin,
                         viewsets.GenericViewSet):
    queryset = ProductReal.objects.all()
    serializer_class = ProductRealSerializer
    pagination_class = LargeResultsSetPagination
    lookup_url_kwarg = 'product_id'




