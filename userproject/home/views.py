from django.shortcuts import render, redirect

# Password for sunny is Sunny@9090
# Create your views here.
def index(request):
    return render(request, "index.html")

def login(request):
    if request.method=="POST":
        # check if user has emtered corret credentials or not
    return render(request, "login.html")

def logout(request):
    return render(request, "logout.html")
