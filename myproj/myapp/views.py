from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse('Hello, f@#ing world!')

def index(request):
    return render(request, 'myapp/index.html', {'index_active': True})

def about(request):
    return render(request, 'myapp/about.html')

def anime_list(request):
    return render(request, 'myapp/anime-list.html', {'anime_list_active': True})