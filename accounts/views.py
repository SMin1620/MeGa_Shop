from django.shortcuts import render
from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from accounts.models import User
from accounts.serialzers import UserSerializer, SignUpSerializer


# Create your views here.
class UserListAPI(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = User.objects.all().order_by('pk')
    serializer_class = UserSerializer


# 회원가입 - 일반 사용자용
class UserCreateAPI(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = SignUpSerializer(data=request.data)

        if not serializer.is_valid(raise_exception=True):
            return Response({
                'message': 'Request Body Error'
            }, status=status.HTTP_409_CONFLICT)

        user = serializer.save()
        token = Token.objects.create(user=user)

        return Response({'Token': token.key}, status=status.HTTP_201_CREATED)

