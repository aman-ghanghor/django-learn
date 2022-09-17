from django.urls import path
from . import views

urlpatterns = [
    path('', views.fees),
    path('fees-python/', views.fees_python),
    path('fees-django/', views.fees_django),
]



