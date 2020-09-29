from django.http.response import Http404
from .models import Question
from django.http import request
from django.http import response
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# from django.template import loader, template
from django.shortcuts import render

# 创建一个视图


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join([q.question_text for q in latest_question_list])
    # template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    # return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    question = get_object_or_404(Question, pk=question_id)
    # return HttpResponse("You're looking at question {}".format(question_id))
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    response = "You're looking at the results of {}"
    return HttpResponse(response.format(question_id))


def vote(request, question_id):
    return HttpResponse("You're voting on question {}".format(question_id))
