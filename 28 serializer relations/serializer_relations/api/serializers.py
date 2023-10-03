
from rest_framework import serializers
from .models import Song, Album

                

class SongSerializer(serializers.ModelSerializer): 
        class Meta: 
                model = Song
                fields = ['id', 'name', 'duration', 'album',]
                
        
class AlbumSerializer(serializers.ModelSerializer): 
        # only adding the realted name would show the PK, but we can customize what do we want to show. 
        
        # show any string of the relation 
        # song = serializers.StringRelatedField(many=True, read_only=True)
        
        # show the link to the associated song object 
        song = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='song-detail') # the view_name shoulbe be : model name _ detail (fixed)
        # song = serializers.PrimaryKeyRelatedField(many=True, read_only=True) # just shows the PK of the related song object 
        # song = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name') # pass the field of which the slug will be built on 
        # sonng = serializers.HyperlinkedIdentityField(many=True, read_only=True, view_name='song-detail') # pass the field of which the slug will be built on 
        class Meta: 
                model = Album
                fields = ['id', 'album_name', 'total_songs', 'song']  # just adding the related_name here, would show the associate PK of the song 