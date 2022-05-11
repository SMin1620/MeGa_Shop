import jwt
from base.settings.common import SECRET_KEY
import rest_framework_simplejwt.exceptions
from django.contrib.auth import get_user
from django.contrib.auth.hashers import check_password
from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer

from accounts.models import User
from accounts.serialzers import UserSerializer, SignUpSerializer, MyTokenObtainPairSerializer


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
    serializer_class = SignUpSerializer

    def create(self, request, *args, **kwargs):
        serializer = SignUpSerializer(data=request.data)

        if not serializer.is_valid(raise_exception=True):
            return Response({
                'message': 'Request Body Error'
            }, status=status.HTTP_409_CONFLICT)

        user = serializer.save()
        token = Token.objects.create(user=user)

        return Response({'Token': token.key}, status=status.HTTP_201_CREATED)


# Token 확장
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


# 로그인 - 일반 사용자용
class UserLoginAPI(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']

        user = User.objects.filter(username=username).first()

        # 만약 username에 맞는 user가 존재하지 않는다면,
        if user is None:
            return Response(
                {"message": "존재하지 않는 아이디입니다."}, status=status.HTTP_400_BAD_REQUEST
            )

        # 비밀번호가 틀린 경우,
        if not check_password(password, user.password):
            return Response(
                {"message": "비밀번호가 틀렸습니다."}, status=status.HTTP_400_BAD_REQUEST
            )

        # user가 맞다면,
        if user is not None:
            token = TokenObtainPairSerializer.get_token(user) # refresh 토큰 생성
            refresh_token = str(token) # refresh 토큰 문자열화
            access_token = str(token.access_token) # access 토큰 문자열화
            response = Response(
                {
                    "user": UserSerializer(user).data,
                    "message": "login success",
                    "token": {
                        "access_token": access_token,
                        "refresh_token": refresh_token
                    },
                },
                status=status.HTTP_200_OK
            )

            response.set_cookie("access_token", access_token, httponly=True)
            response.set_cookie("refresh_token", refresh_token, httponly=True)
            return response
        else:
            return Response(
                {"message": "로그인에 실패하였습니다."}, status=status.HTTP_400_BAD_REQUEST
            )


# 토큰 만료시 refresh 기능
class RefreshTokenAPI(APIView):
    def post(self, request):
        try:
            access_token = request.COOKIES['access_token']
            payload = jwt.decode(access_token, SECRET_KEY, algorithms=['HS256'])
            pk = payload.get('user_id')
            user = get_user(pk)
            serializer = UserSerializer(user)
            response = Response(
                serializer.data,
                status=status.HTTP_200_OK
            )
            response.set_cookie('access_token', access_token)
            response.set_cookie('refresh_token', request.COOKIES['refresh_token'])
            return response

        # 토큰 만료시 토큰 갱신
        except(jwt.exceptions.ExpiredSignatureError):
            try:
                # access token 만료시
                serializer = TokenRefreshSerializer(data={'refresh': request.COOKIES.get('refresh_token', None)})

                if serializer.is_valid(raise_exception=True):
                    access_token = serializer.validated_data['access']
                    refresh_token = request.COOKIES.get('refresh_token', None)
                    payload = jwt.decode(access_token,
                                         SECRET_KEY,
                                         algorithms=['HS256'])
                    pk = payload.get('user_id')
                    user = get_user(pk)
                    serializer = UserSerializer(instance=user)
                    response = Response(serializer.data, status=status.HTTP_200_OK)
                    response.set_cookie('access_token', access_token)
                    response.set_cookie('refresh_token', refresh_token)
                    return response

            except(rest_framework_simplejwt.exceptions.TokenError):
                return Response({"message": "로그인이 만료되었습니다."}, status=status.HTTP_200_OK)

            raise jwt.exceptions.InvalidTokenError

        except(jwt.exceptions.InvalidTokenError):
            return Response({"message": "로그인이 만료되었습니다."}, status=status.HTTP_200_OK)

    # def post(self, request):
    #     refresh_token = request.COOKIES['refresh_token']
    #
    #     if refresh_token is None:
    #         return Response({
    #             "message": "Authentication credentials were not provided."
    #         }, status=status.HTTP_403_FORBIDDEN)
    #
    #     try:
    #         payload = jwt.decode(refresh_token, settings.REFRESH_TOKEN_SECRET, algorithms=['HS256'])
    #     except:
    #         return Response({
    #             "message": "expired refresh token, please login again."
    #         }, status=status.HTTP_403_FORBIDDEN)
    #
    #     user = User.objects.filter(id=payload['user_id']).first()
    #
    #     if user is None:
    #         return Response(
    #             {"message": "user not found"}, status=status.HTTP_400_BAD_REQUEST
    #         )
    #     if not user.is_active:
    #         return Response(
    #             {"message": "user not active"}, status=status.HTTP_400_BAD_REQUEST
    #         )
    #
    #     access_token = generate_access_token(user)







