from django.urls import path, include

from mypage.views import CartReadCreateAPI, CartUpdateDeleteAPI, OrderViewSet


# 장바구니 목록 페이지
cart_list = CartReadCreateAPI.as_view({
    'get': 'list',
})
# 장바구니에 상품 추가
cart_add = CartReadCreateAPI.as_view({
    'post': 'add'
})
# 장바구니 상세 페이지
cart_detail = CartUpdateDeleteAPI.as_view({
    'get': 'retrieve',
    'patch': 'partial_update',
    'delete': 'destroy'
})
# 주문 페이지
order_list = OrderViewSet.as_view({
    'get': 'list'
})


urlpatterns = [
    path('cart/', cart_list),
    path('cart/add/', cart_add),
    path('cart/<int:cart_id>/', cart_detail),
    path('order/', order_list),
]