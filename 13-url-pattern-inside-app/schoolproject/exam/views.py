from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def exam(request):
    return HttpResponse("Exam")

def exam_python(request):
    return HttpResponse("Python Exam")

def exam_django(request):
    return HttpResponse("Django Exam")
