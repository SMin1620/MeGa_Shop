from rest_framework import serializers

from mypage.models import Cart, Order
from accounts.serialzers import UserSerializer
from products.serializers import ProductRealSerializer, ProductSerializer


# 장바구니 시리얼라이저
class CartSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    product_real = ProductRealSerializer(read_only=True)

    class Meta:
        model = Cart
        fields = [
            'id', 'user', 'product_real', 'quantity', 'reg_date', 'update_date'
        ]


# 주문 시리얼라이저
class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    product_real = ProductRealSerializer(read_only=True)

    class Meta:
        model = Order
        fields = [
            'id', 'user', 'product_real', 'quantity', 'reg_date', 'update_date'
        ]

