from multiprocessing import context
from django.shortcuts import render

# Create your views here.

def fees(request):
    return render(request, 'fees/allfees.html')


def fees_python(request):
    data = {'cname':'Python', 'fees': 700}
    return render(request, 'fees/fees.html', context=data)


def fees_django(request):
    data = {'cname':'Django', 'fees': 1500}
    return render(request, 'fees/fees.html', context=data)