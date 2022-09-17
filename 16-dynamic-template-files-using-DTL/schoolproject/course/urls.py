from django.urls import path
from . import views

urlpatterns = [
    path('', views.course),
    path('course-python', views.course_python),
    path('course-django', views.course_django),
]