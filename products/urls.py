from django.urls import path, include

from products.views import ProductReadAPI, ProductDetailAPI

app_name = 'products'

# 상품 목록 페이지 url
product_list = ProductReadAPI.as_view({
    'get': 'list'
})
# 상품 상세 페이지 url
product_detail = ProductDetailAPI.as_view({
    'get': 'retrieve',
})
# 상품 좋아요 url
product_like = ProductDetailAPI.as_view({
    'post': 'like'
})


urlpatterns = [
    path('', product_list),
    path('<int:product_id>/', product_detail),
    path('<int:product_id>/like/', product_like),
]
