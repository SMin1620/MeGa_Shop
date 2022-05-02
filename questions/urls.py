from django.urls import path

from questions.views import QuestionReadCreateAPI, QuestionDetailAPI


# question list
question_list = QuestionReadCreateAPI.as_view({
    'get': 'list',
    'post': 'create'
})

# question detail
question_detail = QuestionDetailAPI.as_view({
    'get': 'retrieve',
    'patch': 'partial_update',
    'delete': 'destroy'
})



urlpatterns = [
    path('', question_list),
    path('<int:question_id>/', question_detail),
]


