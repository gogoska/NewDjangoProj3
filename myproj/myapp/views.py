from django.http import HttpResponse
from django.shortcuts import render
from .models import Anime

def hello(request):
    return HttpResponse('Hello, f@#ing world!')

def index(request):
    return render(request, 'myapp/index.html', {'index_active': True})

def about(request, pk):
    a = Anime.objects.get(pk=pk)
    context = {
        'name': a.name,
        'additional_name': a.additional_name,
        'short_description': a.short_description,
        'large_description': a.large_description,
        'photo': a.photo,
        'main_num_rating': a.main_num_rating,
        'my_top_rating': a.my_top_rating,
    }
    return render(request, 'myapp/about.html', context=context)

def anime_list(request):
    anime_list = Anime.objects.all()
    context = {
        'anime_list_active': True,
        'anime_list': anime_list,
    }
    return render(request, 'myapp/anime-list.html', context=context)