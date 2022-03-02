from rest_framework import serializers

from products.models import Product, ProductCategory
from markets.serializers import MarketSerializer


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

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'display_name', 'price', 'sale_price',
            'is_delete', 'delete_date', 'is_hidden', 'is_sold_out',
            'reg_date', 'update_date', 'category', 'market',
            'hit_count', 'review_count', 'review_point'
        ]
