from django.urls import path

from questions.views import QuestionReadAPI


question_list = QuestionReadAPI.as_view({
    'get': 'list'
})


urlpatterns = [
    path('', question_list),
]

