from django.urls import path
from student.views import shome,exam, get_questions, submit_answers, evaluate



urlpatterns=[
    path('shome',shome,name="shome"),
    path('exam',exam,name="exam"),
    path('get_questions',get_questions,name="get_questions"),
    path('submit_answer',submit_answers,name="submit_answer"),
    path('evaluate/',evaluate,name='evaluate')
    
]