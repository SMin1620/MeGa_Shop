from django.db import models
from django.contrib.contenttypes.fields import GenericRelation

from markets.models import Market
from accounts.models import User
from questions.models import Question, Answer



# Create your models here.
# 카테고리 모델
class ProductCategory(models.Model):
    name = models.CharField('이름', max_length=50)


# 상품 모델
class Product(models.Model):
    name = models.CharField('상품명(내부용)', max_length=100)
    display_name = models.CharField('상품명(노출용)', max_length=100)

    price = models.PositiveIntegerField('판매가')
    sale_price = models.PositiveIntegerField('실제 판매가')

    is_delete = models.BooleanField('삭제 여부', default=False)
    delete_date = models.DateTimeField('삭제 날짜', null=True, blank=True)

    is_hidden = models.BooleanField('노출 여부', default=False)
    is_sold_out = models.BooleanField('품절 여부', default=False)

    reg_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    category = models.ForeignKey(ProductCategory, on_delete=models.DO_NOTHING, related_name='product_category')
    market = models.ForeignKey(Market, on_delete=models.DO_NOTHING, related_name='product_market')

    hit_count = models.PositiveIntegerField('조회수', default=0)
    review_count = models.PositiveIntegerField('리뷰수', default=0)
    review_point = models.PositiveIntegerField('리뷰평점', default=0)

    product_liked_user = models.ManyToManyField(
        User,
        through='products.ProductLikeUser',
        related_name='liked_product'
    )

    question = GenericRelation(Question, on_delete=models.CASCADE)


# 상품 실물 모델
class ProductReal(models.Model):
    reg_date = models.DateTimeField('등록날짜', auto_now_add=True)
    update_date = models.DateTimeField('갱신날짜', auto_now=True)

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_reals")

    option_1_type = models.CharField('옵션1 타입', max_length=10, default='SIZE')
    option_1_name = models.CharField('옵션1 이름(내부용)', max_length=50)
    option_1_display_name = models.CharField('옵션1 이름(고객용)', max_length=50)

    option_2_type = models.CharField('옵션2 타입', max_length=10, default='COLOR')
    option_2_name = models.CharField('옵션2 이름(내부용)', max_length=50)
    option_2_display_name = models.CharField('옵션2 이름(고객용)', max_length=50)

    option_3_type = models.CharField('옵션3 타입', max_length=10, default='', blank=True)
    option_3_name = models.CharField('옵션3 이름(내부용)', max_length=50, default='', blank=True)
    option_3_display_name = models.CharField('옵션3 이름(고객용)', max_length=50, default='', blank=True)

    is_sold_out = models.BooleanField('품절여부', default=False)
    is_hidden = models.BooleanField('노출여부', default=False)

    add_price = models.IntegerField('추가가격', default=0)
    stock_quantity = models.PositiveIntegerField('재고개수', default=0)  # 품절일때 유용함


# 좋아요 모델
class ProductLikeUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    reg_date = models.DateTimeField('좋아요 등록 시간', auto_now_add=True)
    update_date = models.DateTimeField('수정 시간', auto_now=True)



