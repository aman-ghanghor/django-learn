from django.http import HttpResponse

# Create your views here.
def fees(request):
    return HttpResponse("Fees")

def fees_python(request):
    return HttpResponse("Python Fees = 3000")

def fees_django(request):
    return HttpResponse("Django Fees = 1500")

    