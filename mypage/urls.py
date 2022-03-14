from django.urls import path, include

from mypage.views import CartViewSet


cart_list = CartViewSet.as_view({
    'get': 'list'
})
cart_add = CartViewSet.as_view({
    'post': 'add'
})


urlpatterns = [
    path('cart/', cart_list),
    path('cart/add', cart_add),
]