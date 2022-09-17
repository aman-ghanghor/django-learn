from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def course(request):
    return render(request, 'course/allcourse.html')

def course_python(request):
    desc = "Become a Python Programmer and learn one of employer's most requested skills of 2022!This is the most comprehensive, yet straight-forward, course for the Python programming language on Udemy! Whether you have never programmed before, already know basic syntax, or want to learn about the advanced features of Python, this course is for you! In this course we will teach you Python 3."
    name = "Python"
    author = "John Smilga"
    course = {'cname': name, 'desc': desc, 'author': author}
    return render(request, 'course/course.html', context=course)











