import functools
import itertools
from re import search

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render

from .documents import AnimeDocument
from .models import Anime

def hello(request):
    return HttpResponse('Hello, f@#ing world!')

def index(request):
    anime_list_main = Anime.objects.order_by('-main_num_rating')[:5]
    anime_list_my = Anime.objects.order_by('my_top_rating')[:5]

    counter = functools.partial(next, itertools.count()),

    context = {
        'anime_list_main': anime_list_main,
        'anime_list_my': anime_list_my,
        'index_active': True,
        'counter': counter,
    }
    return render(request, 'myapp/index.html', context=context)

def about(request, pk):
    a = Anime.objects.get(pk=pk)
    context = {
        'name': a.name,
        'additional_name': a.additional_name,
        'review': a.review,
        'description': a.description,
        'photo': a.photo,
        'main_num_rating': a.main_num_rating,
        'my_top_rating': a.my_top_rating,
    }
    return render(request, 'myapp/about.html', context=context)

def anime_list(request):
    label_dict = {
        1: 'Объективный топ',
        2: 'Личный топ',
        0: 'По алфавиту',
        3: 'Результат поиска по запросу',
    }

    search_query = request.GET.get('search', None)

    if search_query is not None:
        anime_list = AnimeDocument.search().query(
            "multi_match",
            query=search_query,
            fields= [
                'name',
                'additional_name',
                'review',
                'description',
            ]
        ).to_queryset()

        warning_label = label_dict[3] + f' "{search_query}":'
    else:
        filter = int(request.GET.get('filter', 0))

        if filter == 1:
            anime_list = Anime.objects.order_by('-main_num_rating')
        elif filter == 2:
            anime_list = Anime.objects.order_by('my_top_rating')
        else:
            anime_list = Anime.objects.order_by('name')

        warning_label = label_dict[filter]



    paginator = Paginator(anime_list, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'anime_list_active': True,
        'anime_list': anime_list,
        'warning_label': warning_label,
        "page_obj": page_obj,
    }

    return render(request, 'myapp/anime-list.html', context=context)