from django.shortcuts import render
from rest_framework import mixins, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import action

from mypage.models import Cart, Order
from products.models import ProductReal, Product
from mypage.serializers import CartSerializer, OrderSerializer
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

    # 사용자 별 장바구니 상품 목록
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

    # 장바구니 담기 --> 리액트가 완성되면 테스트
    @action(detail=True, methods='post')
    def add(self, request, *args, **kwargs):
        cart = self.get_object()
        try:
            product_real = Product.objects.get(
                pk=request.data['product_real_id']
            )
            quantity = int(request.data['quantity'])
        except Exception as e:
            print(e)
            return Response({'status': 'fail'})

        existing_product_real = Cart.objects.filter(
            user=request.user,
            product_real=product_real
        ).first()

        if existing_product_real:
            existing_product_real.quantity += quantity
            existing_product_real.save()
        else:
            new_product_real = Cart.objects.create(product_real=product_real, quantity=quantity)
            new_product_real.save()

        serializer = CartSerializer(cart)
        res = {
            'add': serializer.data
        }

        return Response(res)


class OrderViewSet(mixins.ListModelMixin,
                   mixins.UpdateModelMixin,
                   viewsets.GenericViewSet):
    serializer_class = OrderSerializer

    def get_queryset(self):
        user = self.request.user
        return Order.objects.filter(user__id=user.id).all()

    def list(self, request, *args, **kwargs):
        user = self.request.user
        orders = Order.objects.filter(user_id=user.id)

        serializer_order = OrderSerializer(orders, many=True)

        res = {
            'order': serializer_order.data,
        }

        return Response(res)


