from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from rest_framework.decorators import action

from products.models import Product, ProductReal, ProductCategory, ProductLikeUser
from products.serializers import ProductSerializer, ProductRealSerializer, ProductCategorySerializer
from questions.models import Question
from questions.serializers import QuestionReadCreateSerializer, AnswerSerializer
from base.drf.paginations import LargeResultsSetPagination


# Create your views here.
# 상품 목록 - 읽기(read) - 일반 사용자용
class ProductReadAPI(mixins.ListModelMixin,
                     viewsets.GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = LargeResultsSetPagination
    ordering = ['pk']

    # action == list 경우, 상품리스트 페이지에서 모든 카테고리와 상품 데이터를 출력.
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)

        # 카테고리
        categories = ProductCategory.objects.all()
        serializer_cate = ProductCategorySerializer(categories, many=True)

        res = {
            'categories': serializer_cate.data,
            'products': response.data
        }

        return Response(res)


# 상품 상세 페이지 - 읽기(read) - 일반 사용자용
class ProductDetailAPI(mixins.RetrieveModelMixin,
                       viewsets.GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_url_kwarg = 'product_id'

    # 상품 상세 페이지에서 상품에 대한 정보와 옵션들을 출력
    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)

        # 상품 pk
        pk = self.kwargs['product_id']

        # 상품 pk의 옵션들
        options = ProductReal.objects.filter(product_id=pk)
        serializer_option = ProductRealSerializer(options, many=True)

        # question
        product = get_object_or_404(Product, pk=pk)
        ct = ContentType.objects.get_for_model(product)
        questions = Question.objects.filter(
            content_type=ct,
            object_id=pk
        )
        serializer_q = QuestionReadCreateSerializer(questions, many=True)

        res = {
            'product': response.data,
            'options': serializer_option.data,
            'questions': serializer_q.data
        }

        return Response(res)

    # 좋아요
    @action(detail=True, methods='post')
    def like(self, request, *args, **kwargs):
        user = self.request.user
        pk = self.kwargs['product_id']

        product = get_object_or_404(Product, pk=pk)

        # 만약 user가 product를 좋아요를 이미 했다면,
        if product.product_liked_user.filter(pk=pk).exists():
            product.product_liked_user.remove(user)
        # 하지 않았다면,
        else:
            product.product_liked_user.add(user)

        return Response(status=status.HTTP_200_OK)


# # 상품 리스트 - 일반 사용자용
# class ProductReadAPI(mixins.ListModelMixin,
#                      mixins.RetrieveModelMixin,
#                      mixins.CreateModelMixin,
#                      viewsets.GenericViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     pagination_class = LargeResultsSetPagination
#     lookup_url_kwarg = 'product_id'
#
#     # action == list 경우, 상품리스트 페이지에서 모든 카테고리와 상품 데이터를 출력.
#     def list(self, request, *args, **kwargs):
#         response = super().list(request, *args, **kwargs)
#         category = ProductCategory.objects.all()
#         serializer = ProductCategorySerializer(category, many=True)
#
#         # 좋아요
#
#         res = {
#             'category': serializer.data,
#             'product': response.data
#         }
#         return Response(res)
#
#     # action == retrieve 경우, 상품디테일 페이지에서 pk상품 데이터와 option 데이터를 출력.
#     def retrieve(self, request, *args, **kwargs):
#         product_id = self.kwargs['product_id']
#         option = ProductReal.objects.filter(product_id=product_id)
#         serializer_option = ProductRealSerializer(option, many=True)
#
#         instance = self.get_object()
#         serializer = self.get_serializer(instance)
#
#         # 상품의 질문
#         product = Product.objects.get(pk=product_id)
#         ct = ContentType.objects.get_for_model(product)
#         question = Question.objects.filter(
#             content_type=ct,
#             object_id=product.id
#         )
#         serializer_question = QuestionSerializer(question, many=True)
#
#         # 좋아요
#         # liked = ProductLikeUser.objects.filter(user=request.user, product=product).count()
#
#         res = {
#             'product': serializer.data,
#             'product_real': serializer_option.data,
#             'question': serializer_question.data,
#         }
#
#         return Response(res)
#
#     ###### page not found 404 ㅠㅠ error --> /{pk}/에서 post로 작동함.
#     # action == post 경우, user <-> product : Like
#     @action(detail=True, methods=['post'])
#     def like(self, request, *args, **kwargs):
#         pk = kwargs['product_id']
#         user = request.user
#         product = get_object_or_404(Product, pk=pk)
#
#         # user 와 product 의 like 관계 확인
#         # 만약 user가 이미 product를 like 했다면,
#         if product.product_liked_user.filter(pk=pk).exists():
#             # 좋아요 취소
#             product.product_liked_user.remove(user)
#         else:
#             product.product_liked_user.add(user)
#
#         return Response(status=status.HTTP_200_OK)
#
#     # qna 생성
#     # def question(self, request, *args, **kwargs):
#     #     pk = kwargs['product_id']


# 카테고리 별 상품리스트
class ProductCategoryAPI(mixins.ListModelMixin,
                         viewsets.GenericViewSet):
    lookup_url_kwarg = 'category_id'
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    # action == list 경우, 카테고리 pk 필터링.
    def list(self, request, *args, **kwargs):
        category_id = self.kwargs['category_id']
        category_id = self.kwargs['category_id']
        product = Product.objects.filter(category_id=category_id)
        serializer_product = ProductSerializer(product, many=True)
        category = ProductCategory.objects.all()
        serializer_cate = ProductCategorySerializer(category, many=True)

        res = {
            'categories': serializer_cate.data,
            'products': serializer_product.data
        }

        return Response(res)








