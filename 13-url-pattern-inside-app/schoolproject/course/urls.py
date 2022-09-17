from django.urls import path
from . import views

urlpatterns = [
    path('', views.course),
    path('learn-python/', views.learn_python),
    path('learn-django/', views.learn_django)
]







