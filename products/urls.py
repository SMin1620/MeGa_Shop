from django.urls import path, include

from products.views import ProductReadAPI, ProductDetailAPI

app_name = 'products'

# 상품 리스트 url
product_list = ProductReadAPI.as_view({
    'get': 'list'
})
#상품 디테일 url
product_detail = ProductDetailAPI.as_view({
    'get': 'retrieve',
})
# 상품 좋아요
product_like = ProductDetailAPI.as_view({
    'post': 'like'
})
#
# # 카테고리 별 상품 리스트
# product_category_list = ProductCategoryAPI.as_view({
#     'get': 'list'
# })

urlpatterns = [
    path('', product_list),
    path('<int:product_id>/', product_detail),
    path('<int:product_id>/like/', product_like),
    # path('category/<int:category_id>/', product_category_list),
]
