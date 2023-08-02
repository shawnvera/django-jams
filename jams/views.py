from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import GenreSerializer, ArtistSerializer, AlbumSerializer, SongSerializer

class GenreViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows genres to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [permissions.AllowAny]

class ArtistViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows artists to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [permissions.AllowAny]

class AlbumViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows albums to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = [permissions.AllowAny]


class SongViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows songs to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = SongSerializer
    permission_classes = [permissions.AllowAny]