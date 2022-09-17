from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def course(request):
    return render(request, 'course.html')

def course_python(request):
    return HttpResponse("Python Course")

def course_django(request):
    return HttpResponse("Django Course")

