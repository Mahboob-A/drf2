from django.contrib import admin

# Register your models here.
from .models import Song, Album


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin): 
        list_display = ['id', 'album_name', 'total_songs']
        

@admin.register(Song) 
class SongAdmin(admin.ModelAdmin):
        list_display = ['id', 'name', 'duration', 'album']
        