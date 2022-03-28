from rest_framework import serializers

from questions.models import Question, Answer
from accounts.serialzers import UserSerializer


# 질문 시리얼라이저
class QuestionSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Question
        fields = '__all__'


# 답변 시리얼라이저
class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'
