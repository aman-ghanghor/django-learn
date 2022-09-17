from django import http
from django.http import HttpResponse

# Create your views here.

def course(request):
    return HttpResponse("Course")

def learn_python(request):
    return HttpResponse("Learn Python")

def learn_django(request):
    return HttpResponse("Learn Django")