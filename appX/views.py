from django.shortcuts import render
from django.http import HttpResponse

from . import models
# Create your views here.


def sample(request):
	return HttpResponse("This is a sample view")

def listing(request):
	listt = ["apple","banana","carrot","dates","elderberry"]
	context ={"list": listt}
	return render(request,'listing.html',context)

def home(request):
	latest_question_list = models.Question.objects.order_by('-pub_date')[:5]
	context = {"latest_questions" : latest_question_list}
	return render(request,"home.html",context)

def question(request,question_id):
	question = models.Question.objects.get(pk=question_id)
	answers = question.answer_set.all()
	context = {"question":question , "answers" : answers}
	return render(request,"question.html",context)