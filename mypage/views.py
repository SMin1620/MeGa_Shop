import json

from django.shortcuts import get_object_or_404
from rest_framework import mixins, viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from mypage.models import Cart, Order
from mypage.serializers import CartSerializer, OrderSerializer, CartDetailSerializer, CartAddSerializer
from products.serializers import ProductRealSerializer


# Create your views here.
# 장바구니 - 읽기(READ), 추가(POST) - 일반 사용자용
class CartReadCreateAPI(mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    lookup_field = 'product_real_id'

    def get_serializer_class(self):
        if self.request.method == 'get':
            return CartSerializer
        else:
            return CartAddSerializer

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

    # 장바구니 담기
    @action(detail=False, methods='post')
    def add(self, request, *args, **kwargs):
        user = self.request.user
        product_real = request.POST.get('product_real')
        quantity = request.POST.get('quantity')

        # 장바구니에 상품이 이미 존재한다면,
        if Cart.objects.filter(product_real_id=product_real).exists():
            cart = get_object_or_404(Cart, product_real_id=product_real)
            cart.quantity = str(int(cart.quantity) + int(quantity))
            cart.save()
        # 존재하지 않는다면,
        else:
            cart = Cart(
                user=user,
                product_real_id=product_real,
                quantity=quantity
            )
            cart.save()

        return Response(status=status.HTTP_201_CREATED)





    # # 장바구니 담기 --> 리액트가 완성되면 테스트
    # @action(detail=False, methods='post')
    # def add(self, request, *args, **kwargs):
    #     cart = self.get_object()
    #
    #     try:
    #         product_real = Product.objects.get(
    #             pk=request.data['product_real_id']
    #         )
    #         quantity = int(request.data['quantity'])
    #     except Exception as e:
    #         print(e)
    #         return Response({'status': 'fail'})
    #
    #     existing_product_real = Cart.objects.filter(
    #         user=request.user,
    #         product_real=product_real
    #     ).first()
    #
    #     if existing_product_real:
    #         existing_product_real.quantity += quantity
    #         existing_product_real.save()
    #     else:
    #         new_product_real = Cart.objects.create(product_real=product_real, quantity=quantity)
    #         new_product_real.save()
    #
    #     serializer = CartSerializer(cart)
    #     res = {
    #         'add': serializer.data
    #     }
    #
    #     return Response(res)


# 장바구니 - 읽기(RETRIEVE), 수정(PATCH), 삭제(DELETE) - 일반 사용자용
class CartUpdateDeleteAPI(mixins.RetrieveModelMixin,
                          mixins.UpdateModelMixin,
                          mixins.DestroyModelMixin,
                          viewsets.GenericViewSet):
    serializer_class = CartDetailSerializer
    lookup_url_kwarg = 'cart_id'

    def get_queryset(self):
        user = self.request.user
        return Cart.objects.filter(user_id=user.id).all()

    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)

        res = {
            'product': response.data
        }

        return Response(res)






# 주문 리스트
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

        # 주문 상품 총 가격
        total_price = 0
        for order in orders:
            total_price += (
                                   order.product_real.product.sale_price
                                   +
                                   order.product_real.add_price
                           ) * order.quantity

        res = {
            'order': serializer_order.data,
            'total_price': total_price
        }

        return Response(res)
