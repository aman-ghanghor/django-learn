from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def get_fees(request):
    return HttpResponse("Hello Fees")