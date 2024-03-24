from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("This is Home Page")

def about(request):
    return HttpResponse("This is About")

def services(request):
    return HttpResponse("This is services")

def contact(request):
    return HttpResponse("This is contact")
