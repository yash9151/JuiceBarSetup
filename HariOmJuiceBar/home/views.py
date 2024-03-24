from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        "variable1" :"This is Yash",
        "variable2" :"This is Sunny"
    }
    return render(request, "index.html", context)
    # return render(request, "index.html")
    # return HttpResponse("This is Home Page")

def about(request):
    return HttpResponse("This is About")

def services(request):
    return HttpResponse("This is services")

def contact(request):
    return HttpResponse("This is contact")
