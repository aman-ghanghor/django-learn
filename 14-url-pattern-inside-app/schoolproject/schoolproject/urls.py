"""schoolproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from course import views as course_v
from fees import views as fees_v
from exam import views as exam_v


exam_urlpatterns = [
    path('exam-python/', exam_v.exam_python),
    path('exam-django/', exam_v.exam_django),
]


urlpatterns = [
    path('admin/', admin.site.urls),

    path('mycourse/', course_v.course),
    path('mycourse/', include([
        path('course-python/', course_v.course_python),
        path('course-django/', course_v.course_django),
    ])),

    path('myfees/', fees_v.fees),
    path('myfees/', include([
        path('fees-python/', fees_v.fees_python),
        path('fees-django/', fees_v.fees_django),
    ])),

    path('myexam/', exam_v.exam),
    path('myexam/', include(exam_urlpatterns)),
]
