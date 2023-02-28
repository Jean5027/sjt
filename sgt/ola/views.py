from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1 style=\"color:aqua\">olá mundo!</h1>")

def greet(request, name):
    return HttpResponse(f"Hello, {name}!")

def index(request):
    return render(request, "index.html")
