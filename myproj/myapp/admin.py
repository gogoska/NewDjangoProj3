from django.contrib import admin
from .models import Anime

class AnimeAdmin(admin.ModelAdmin):
	list_display = ('name', 'main_num_rating', 'my_top_rating')
	list_display_links = ('name',)
	search_fields = ('name',)
	list_editable = ('main_num_rating', 'my_top_rating')
	list_filter = ('name', 'main_num_rating', 'my_top_rating')


admin.site.register(Anime, AnimeAdmin)