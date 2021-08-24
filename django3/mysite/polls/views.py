from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question
from django.template import loader
from django.http import Http404
# Create your views here.

def index(request):
    # 第一版
    # latst_question_list=Question.objects.order_by('-pub_date')[:5]
    # output=','.join([q.question_text for q in latst_question_list])
    # return HttpResponse(output)

    #第二版，添加链接， 指向问题的详细页
    # latest_question_list=Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    # context = {
    #     'latest_question_list': latest_question_list
    # }
    # return HttpResponse(template.render(context,request))

    #第三版，使用render
    latest_question_list=Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list
    }
    return render(request,'polls/index.html',context)

    
def detail(request, question_id):
    #第一版
    # return HttpResponse("You're looking at question %s. " %question_id)

    #第二版，问题不存在时弹出404
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404('Question does not exist.')
    # return render(request,'polls/detail.html',{'question':question})

    # 第三版，使用get_object_or_404函数
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/detail.html',{'question':question})




def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response %question_id)

def vote(request, question_id):
    return HttpResponse("you're voting on question %s." %question_id)