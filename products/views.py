from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from products.models import Product, ProductReal, ProductCategory
from products.serializers import ProductSerializer, ProductRealSerializer, ProductCategorySerializer
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

    # action == list 경우, 상품리스트 페이지에서 모든 카테고리와 상품 데이터를 출력.
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        category = ProductCategory.objects.all()
        serializer = ProductCategorySerializer(category, many=True)

        res = {
            'category': serializer.data,
            'product': response.data
        }
        return Response(res)

    # action == retrieve 경우, 상품디테일 페이지에서 pk상품 데이터와 option 데이터를 출력.
    def retrieve(self, request, *args, **kwargs):
        product_id = self.kwargs['product_id']
        option = ProductReal.objects.filter(product_id=product_id)
        serializer_option = ProductRealSerializer(option, many=True)

        instance = self.get_object()
        serializer = self.get_serializer(instance)

        res = {
            'product': serializer.data,
            'option': serializer_option.data
        }

        return Response(res)





