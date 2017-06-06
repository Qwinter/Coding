from django.http import HttpResponse
from django.shortcuts import render

from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def results(request, qustion_id):
    response = "你正在看问题的结果 %s"
    return  HttpResponse(response  % qustion_id)

def vote(request, question_id):
    return HttpResponse(" 你投票的问题 %s " % question_id)