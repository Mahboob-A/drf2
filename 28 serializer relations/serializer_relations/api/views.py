from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets 
from .models import Song, Album
from .serializers import SongSerializer, AlbumSerializer



class AlbumViewSet(viewsets.ModelViewSet): 
        queryset = Album.objects.all()
        serializer_class = AlbumSerializer
        
        
class SongViewSet(viewsets.ModelViewSet): 
        queryset = Song.objects.all()
        serializer_class = SongSerializer 
        
