from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def fees(request):
    return render(request, 'fees.html')

def fees_python(request):
    return HttpResponse("Python fees")

def fees_django(request):
    return HttpResponse("Django fees")

