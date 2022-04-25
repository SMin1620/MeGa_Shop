from rest_framework import serializers

from products.models import Product, ProductCategory, ProductReal
from markets.serializers import MarketSerializer


# 상품 카테고리 시리얼라이저, 읽기전용
class ProductCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductCategory
        fields = [
            'id', 'name'
        ]


# 상품 시리얼라이저, 읽기전용
class ProductSerializer(serializers.ModelSerializer):
    category = ProductCategorySerializer(read_only=True)
    market = MarketSerializer(read_only=True)
    # product_reals = ProductRealSerializer(many=True)

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'display_name', 'price', 'sale_price',
            'is_hidden', 'is_sold_out',
            'reg_date', 'update_date', 'category', 'market',
            'hit_count', 'review_count', 'review_point', 'product_liked_user'
        ]


# 상품 옵션 시리얼라이저, 읽기전용
class ProductRealSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = ProductReal
        fields = [
            'id', 'option_1_type', 'option_1_display_name', 'option_2_type',
            'option_2_display_name', 'option_3_type', 'option_3_display_name',
            'is_sold_out', 'add_price', 'stock_quantity', 'product'
        ]


# 상품 장바구니 담기 시리얼라이저
class ProductReadCartAddSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductReal
        fields = [
            'id'
        ]
        write_fields = [
            'stock_quantity'
        ]
