from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello, f@#ing world!")

def index(request):
    return render(request, "myapp/index.html")
