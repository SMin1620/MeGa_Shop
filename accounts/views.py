from django.shortcuts import render
from rest_framework import viewsets, mixins

from accounts.models import User
from accounts.serialzers import UserSerializer


# Create your views here.
class UserListAPI(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = User.objects.all().order_by('pk')
    serializer_class = UserSerializer
