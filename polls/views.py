from django.shortcuts import render
from django.http import HttpResponse

from .models import Question
# Create your views here.

def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	output = ", ".join([p.question_text for p in latest_question_list])
	return HttpResponse("Hello, world. You're at the polls index %s" % output)
	
def detail(request, question_id):
	return HttpResponse("This page is details for question %s" % question_id)
	
def results(request, question_id):
	return HttpResponse("This page is results for question %s" % question_id)
	
def vote(request, question_id):
	return HttpResponse("This page is votes for question %s" % question_id)