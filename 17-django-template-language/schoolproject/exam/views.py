from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def exam(request):
    return render(request, 'other/exam.html')

def exam_python(request):
    return HttpResponse("Python Exam")

def exam_django(request):
    return HttpResponse("Django Exam")

