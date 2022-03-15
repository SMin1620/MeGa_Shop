from django.contrib import admin

from mypage.models import Cart, Order

# Register your models here.
admin.site.register(Cart)
admin.site.register(Order)