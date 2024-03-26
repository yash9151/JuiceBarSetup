from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages


# Create your views here.
def index(request):
    context = {
        "variable1" :"This is Yash",
        "variable2" :"This is Sunny"
    }
    # messages.success(request,"Hello")
    return render(request, "index.html", context)
    # return render(request, "index.html")
    # return HttpResponse("This is Home Page")

def about(request):
    # return HttpResponse("This is About")
    return render(request, "about.html")

def services(request):
    # return HttpResponse("This is services")
    return render(request, "services.html")

def contact(request):
    # return HttpResponse("This is contact")
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, "Cheers!!! Your message has been sent to admin.")
    return render(request, "contact.html")
