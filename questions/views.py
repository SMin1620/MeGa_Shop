from django.shortcuts import render
from rest_framework import mixins, viewsets
from rest_framework.response import Response

from questions.models import Question, Answer
from questions.serializers import QuestionReadCreateSerializer, QuestionDetailSerializer, QuestionUpdateSerializer


# Create your views here.
# 질문 리스트 - 조회, 생성 - 일반 사용자용
class QuestionReadCreateAPI(mixins.ListModelMixin,
                            mixins.CreateModelMixin,
                            viewsets.GenericViewSet):
    serializer_class = QuestionReadCreateSerializer
    queryset = Question.objects.all()

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)

        res = {
            'question': response.data
        }

        return Response(res)

    # 질문 생성 커스텀
    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)


# 질문 디테일 - 조회, 수정, 삭제 - 일반 사용자용
class QuestionDetailAPI(mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionDetailSerializer
    lookup_url_kwarg = 'question_id'

    # 단일 조회 - 일반 사용자용
    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        user = self.request.user

        res = {
            'question': response.data
        }

        return Response(res)













