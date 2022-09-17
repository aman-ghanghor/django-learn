from calendar import month
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from datetime import datetime


def course(request):
    courses = {'allcourses': ['Python', 'Django']}
    return render(request, 'course/allcourses.html', context=courses)


def course_python(request):
    desc = "This python for beginners course is geared to students who want to know how python works and also to those totally new to programming. The python language has very simple syntax(way to write it) to learn and it is one of the most powerful languages to learn since it can used for a variety of things."
    dt = datetime(year=2020, month=8, day=23)
    print(dt)

    course = {'cname': 'Python', 'duration': '6 Months', 'seats': 10, 'price': "3000.6758", 'desc': desc, 'upload_date': dt}
    return render(request, 'course/course.html', context=course)



def students(request):
    # student = {'names': ['rahul', 'sonam', 'raj', 'anu']}
    stu = {
        'stu1': {'name': 'Rahul', 'roll': 101},
        'stu2': {'name': 'Sonam', 'roll': 102},
        'stu3': {'name': 'Raj', 'roll': 103},
        'stu4': {'name': 'Anu', 'roll': 104}
    }
    students = {'student': stu}
    return render(request, 'course/students.html', context=students)



def course_django(request):
    courname = {'cname': 'Django', 'duration': '2 Months', 'seats': 45, 'price': "Rs. 5500"}
    return render(request, 'course/course.html', context=courname)

