
from django.db import models
import os



# Create your models here.

class Anime(models.Model):
    name = models.CharField(max_length=90, verbose_name='Название')
    additional_name = models.CharField(max_length=250, verbose_name='Доп. название', blank=True)
    # short_description = models.TextField(verbose_name='Краткое описание', blank=True)
    # large_description = models.TextField(verbose_name='Длинное описание', blank=True)
    review = models.TextField(verbose_name='Отзыв', blank=True)
    description = models.TextField(verbose_name='Описание', blank=True)
    photo = models.ImageField(upload_to='anime-img/%Y/%m/%d/', verbose_name='Картика', blank=True)
    main_num_rating = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Главный рейтинг')
    my_top_rating = models.IntegerField(verbose_name='Мой рейтинг')

    class Meta:
        verbose_name = 'Аниме'
        verbose_name_plural = 'Анимешки'
        ordering = ['name']

