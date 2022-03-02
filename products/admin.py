from django.contrib import admin

from products.models import Product, ProductCategory, ProductReal

# Register your models here.
admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(ProductReal)
