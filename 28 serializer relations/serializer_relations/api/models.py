from django.db import models

# Create your models here.


class Album(models.Model): 
        singer_name = models.CharField(max_length=30)
        album_name = models.CharField(max_length=30)
        total_songs = models.IntegerField()
        
        def __str__(self): 
                return self.album_name
        

class Song(models.Model): 
        album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='song')
        name = models.CharField(max_length=30)
        duration = models.DecimalField(max_digits=3, decimal_places=2)
        
        def __str__(self) -> str:
                return self.name 
        
        