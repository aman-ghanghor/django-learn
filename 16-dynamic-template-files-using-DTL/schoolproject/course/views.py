from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def course(request):
    courses = {'allcourses': ['Python', 'Django']}
    return render(request, 'course/allcourses.html', context=courses)

def course_python(request):
    courname = {'cname': 'Python', 'duration': '6 Months', 'seats': 10, 'price': "Rs. 3000"}
    return render(request, 'course/course.html', context=courname)

def course_django(request):
    courname = {'cname': 'Django', 'duration': '2 Months', 'seats': 45, 'price': "Rs. 5500"}
    return render(request, 'course/course.html', context=courname)

