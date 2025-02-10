from django.db import models

# Create your models here.

class Anime(models.Model):
    name = models.CharField(max_length=90)
    additional_name = models.CharField(max_length=250)
    short_description = models.TextField()
    large_description = models.TextField()
    photo = models.ImageField(upload_to ='anime-img/%Y/%m/%d/')
    main_num_rating = models.DecimalField(max_digits=10, decimal_places=2)
    my_top_rating = models.IntegerField()

