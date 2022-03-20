from django.contrib import admin

from products.models import Product, ProductCategory, ProductReal, ProductLikeUser

# Register your models here.
admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(ProductReal)
admin.site.register(ProductLikeUser)
