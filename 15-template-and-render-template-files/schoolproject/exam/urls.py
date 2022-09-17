from django.urls import path
from . import views

urlpatterns = [
    path('', views.exam),
    path('exam-python', views.exam_python),
    path('exam-django', views.exam_django),
]