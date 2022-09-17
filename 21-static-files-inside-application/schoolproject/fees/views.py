import re
from django.shortcuts import render

# Create your views here.

def fees(request):
    return render(request, 'fees/allfees.html')

def fees_python(request):
    return render(request, 'fees/fees.html')



