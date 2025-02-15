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
    filter = int(request.GET.get('filter', 0))

    filter_dict = {
        1: 'Объективный топ',
        2: 'Личный топ',
        0: 'По алфавиту',
    }

    if filter == 1:
        anime_list = Anime.objects.order_by('-main_num_rating')
    elif filter == 2:
        anime_list = Anime.objects.order_by('my_top_rating')
    else:
        anime_list = Anime.objects.order_by('name')

    filter_label = filter_dict[filter]

    context = {
        'anime_list_active': True,
        'anime_list': anime_list,
        'filter_label': filter_label,
    }

    return render(request, 'myapp/anime-list.html', context=context)