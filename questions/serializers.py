from rest_framework import serializers

from questions.models import Question, Answer
from accounts.serialzers import UserSerializer


# 답변 시리얼라이저
class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


# 질문 시리얼라이저 - 조회, 생성 - 읽기전용
class QuestionReadCreateSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    answer = AnswerSerializer(read_only=True)

    class Meta:
        model = Question
        fields = '__all__'


# 질문 시리얼라이저 - 조회, 삭제 - 읽기전용
class QuestionDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    answer = AnswerSerializer(read_only=True)

    class Meta:
        model = Question
        read_only_fields = [
            'id', 'user', 'content_type', 'object_id', 'content_object', 'is_complete',
            'reg_date', 'update_date', 'answer'
        ]
        fields = '__all__'


# 질문 시리얼라이저 - 수정 - 읽기 전용
class QuestionUpdateSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Question
        read_only_fields = [
            'id', 'user', 'content_type', 'object_id', 'content_object', 'is_complete',
            'reg_date', 'update_date'
        ]
        fields = [
            'content'
        ]
