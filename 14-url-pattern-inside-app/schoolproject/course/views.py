from django import http
from django.http import HttpResponse

# Create your views here.

def course(request):
    return HttpResponse("Course")

def course_python(request):
    return HttpResponse("Python Course")

def course_django(request):
    return HttpResponse("Django Course")