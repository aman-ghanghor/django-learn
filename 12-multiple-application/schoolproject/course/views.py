from django import http
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def get_course(request):
    return HttpResponse("Hello Course")
