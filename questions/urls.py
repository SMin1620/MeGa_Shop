from django.urls import path

from questions.views import QuestionReadAPI

# test용
question_list = QuestionReadAPI.as_view({
    'get': 'list'
})


urlpatterns = [
    path('', question_list),
]


