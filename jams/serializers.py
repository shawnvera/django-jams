from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *


class GenreSerializer(serializers.Serializer):
    class Meta:
        model = Genre
        fields = '__all__'

class ArtistSerializer(serializers.Serializer):
    class Meta:
        model = Artist
        fields = '__all__'


class AlbumSerializer(serializers.Serializer):
    class Meta:
        model = Album
        fields = '__all__'


class SongSerializer(serializers.Serializer):
    class Meta:
        model = Song
        fields = '__all__'



        
    # email = serializers.EmailField()
    # content = serializers.CharField(max_length=200)
    # created = serializers.DateTimeField()