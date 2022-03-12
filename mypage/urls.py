from django.urls import path, include

from mypage.views import CartViewSet


cart_list = CartViewSet.as_view({
    'get': 'list'
})


urlpatterns = [
    path('cart/', cart_list),
]