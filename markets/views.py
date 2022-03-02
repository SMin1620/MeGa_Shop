from django.shortcuts import render
from rest_framework.generics import mixins
from rest_framework import viewsets

from markets.models import Market
from markets.serializers import MarketSerializer


# Create your views here.
# 마켓 리스트
class MarketListAPI(mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):
    queryset = Market.objects.all()
    serializer_class = MarketSerializer