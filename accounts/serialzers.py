from django.contrib.auth import authenticate
from rest_framework import serializers

from accounts.models import User


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
class UserLoginSerializer(serializers.ModelSerializer):
    def validate(self, data):
        username = data.get('username', None)
        password = data.get('password', None)
        user = authenticate(username=username, password=password)

        # user가 없다면,
        if user is None:
            return {'id': 'None', 'username': username}

        #

