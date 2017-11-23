from django.shortcuts import render

from django.http import HttpResponse
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])

    return HttpResponse(output)



def detail(request, question_id):
    return HttpResponse('You are looking at question {}'.format(question_id))

def results(request, question_id):
    response = "you are looking at results of question {}".format(question_id)
    return HttpResponse(response)


def vote(request, question_id):
    return HttpResponse("you ar voting on question {}".format(question_id))