from django.shortcuts import render
from rest_framework import mixins, viewsets
from rest_framework.response import Response

from questions.models import Question, Answer
from questions.serializers import QuestionSerializer



# Create your views here.
# 질문 리스트 - 확인용
class QuestionReadAPI(mixins.ListModelMixin,
                      viewsets.GenericViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)

        res = {
            'question': response.data
        }

        return Response(res)




