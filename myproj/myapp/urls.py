from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('hello', hello),
    path('about/<int:pk>', about, name='about'),
    path('anime-list', anime_list, name='anime-list'),
]