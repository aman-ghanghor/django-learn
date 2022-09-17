from calendar import c
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def course(request):
    return render(request, 'course/allcourse.html')

def course_python(request):
    return render(request, 'course/course.html')











