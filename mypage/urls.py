from django.urls import path, include

from mypage.views import CartViewSet, OrderViewSet


cart_list = CartViewSet.as_view({
    'get': 'list'
})
cart_add = CartViewSet.as_view({
    'post': 'add'
})

order_list = OrderViewSet.as_view({
    'get': 'list'
})


urlpatterns = [
    path('cart/', cart_list),
    path('cart/add', cart_add),
    path('order/', order_list),
]