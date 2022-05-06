from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework import serializers
from rest_framework.settings import api_settings
from rest_framework_simplejwt.serializers import TokenObtainSerializer

from accounts.models import User

# JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
# JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 'name', 'profile_img', 'gender', 'created_at', 'modified_at',
        ]


# 회원가입 시리얼라이저 - 일반 사용자용
class SignUpSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
            name=validated_data['name']
        )

        user.save()
        return user

    class Meta:
        model = User
        fields = [
            'username', 'password', 'email', 'name', 'gender'
        ]


# 로그인 시리얼라지ㅓ - 일반 사용자용
# class UserLoginSerializer(serializers.ModelSerializer):
#     def validate(self, data):
#         username = data.get('username', None)
#         password = data.get('password', None)
#         user = authenticate(username=username, password=password)
#
#         # user가 없다면,
#         if user is None:
#             return {'id': 'None', 'username': username}
#
#         try:
#             payload = JWT_PAYLOAD_HANDLER(user)
#             jwt_token = JWT_ENCODE_HANDLER(payload)  # 토큰 발행
#             update_last_login(None, user)
#         except User.DoesNotExist:
#             raise serializers.ValidationError(
#                 'User with given email and password does not exists'
#             )
#
#         return {
#             'username': user.username,
#             'token': jwt_token
#         }


# 토큰 발급 확장
class MyTokenObtainPairSerializer(TokenObtainSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['is_staff'] = user.is_staff
        token['is_superuser'] = user.is_superuser
        token['token'] = user.token
        return token


