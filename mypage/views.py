from django.shortcuts import render
from rest_framework import mixins, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from mypage.models import Cart
from products.models import ProductReal
from mypage.serializers import CartSerializer
from products.serializers import ProductRealSerializer


# Create your views here.
# 장바구니 리스트
class CartViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    serializer_class = CartSerializer

    def get_queryset(self):
        user = self.request.user
        return Cart.objects.filter(user_id=user.id).all()

    def list(self, request, *args, **kwargs):
        user = self.request.user
        carts = Cart.objects.filter(user__id=user.id).all()
        total_price = 0

        serializer = CartSerializer(carts, many=True)

        for cart in carts:
            total_price += (cart.product_real.product.sale_price + cart.product_real.add_price) * cart.quantity

        res = {
            'cart': serializer.data,
            'total_price': total_price
        }

        return Response(res)


