from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def course(request):
    return HttpResponse("<h1> Learn Courses </h1>")

def learn_django(request):
    return HttpResponse("<h1> Learn Django </h1>")

def learn_python(request):
    return HttpResponse("<h1> Learn Python </h1>")