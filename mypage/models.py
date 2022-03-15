from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from accounts.models import User
from products.models import Product, ProductReal


# Create your models here.
# 장바구니 모델
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_real = models.ForeignKey(ProductReal, on_delete=models.CASCADE)

    reg_date = models.DateTimeField('등록 날짜', auto_now_add=True)
    update_date = models.DateTimeField('수정 날짜', auto_now=True)
    quantity = models.PositiveIntegerField('수량', default=1, validators=[MinValueValidator(1), MaxValueValidator(100)])


# 주문 모델
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_real = models.ForeignKey(ProductReal, on_delete=models.CASCADE)

    quantity = models.PositiveIntegerField('수량')
    reg_date = models.DateTimeField('주문 등록 날짜', auto_now_add=True)
    update_date = models.DateTimeField('수정 날짜', auto_now=True)


