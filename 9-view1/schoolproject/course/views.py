from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def django_course(request):
    return HttpResponse("<h1> Hello World </h1>")


def django_learn(request):
    return HttpResponse("<h1> Django Learn </h1>")