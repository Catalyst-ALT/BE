from rest_framework import generics, permissions
# from django.shortcuts import render, get_object_or_404
from .models import User, Write, VisualArt, Movement, Music
from .serializers import MusicInputSerializer, MusicOutputSerializer, WriteInputSerializer, ProfileSerializer, WriteOutputSerializer, VisualArtInputSerializer, VisualArtOutputSerializer, MovementInputSerializer, MovementOutputSerializer
from catalyst.permissions import IsProfileOwnerOrReadOnly
import time


class ProfileViewSet(generics.RetrieveUpdateDestroyAPIView):
    '''
    Methods: GET, PATCH, DELETE
    PATCH and DELETE methods only able to be performed by profile owner
    '''
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = "username"
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsProfileOwnerOrReadOnly]


class WriteInputViewSet(generics.CreateAPIView):
    '''
    METHODS: POST
    Creates user input/prompt instance to send to openai's api
    Calls get_write_length() function to get user inputted prompt length
    Calls send_write_prompt() function to connect call openai's api
    Asynch - 1 second delay between calling the 2 functions
    '''
    queryset = Write.objects.all()
    serializer_class = WriteInputSerializer

    def perform_create(self, serializer):
        poem = serializer.save()
        length = serializer.save()

        length.get_write_length()
        time.sleep(1)
        poem.send_write_prompt()


class WriteOutputViewSet(generics.RetrieveAPIView):
    '''
    METHODS: GET
    Retrieves Write instance from the database (including 'output' which has now been supplied by openai's api)
    '''
    queryset = Write.objects.all()
    serializer_class = WriteOutputSerializer


class VisualArtInputViewSet(generics.CreateAPIView):
    '''
    METHODS: POST
    Creates user input/prompt instance to send to openai's api
    Calls get_visual_art_length() function to get user inputted prompt length
    Calls send_visual_art_prompt() function to connect call openai's api
    Asynch - 1 second delay between calling the 2 functions
    '''
    queryset = VisualArt.objects.all()
    serializer_class = VisualArtInputSerializer

    def perform_create(self, serializer):
        visualart = serializer.save()
        length = serializer.save()

        length.get_visual_art_length()
        time.sleep(1)
        visualart.send_visual_art_prompt()


class VisualArtOutputViewSet(generics.RetrieveAPIView):
    '''
    METHODS: GET
    Retrieves VisualArt instance from the database (including 'output' which has now been supplied by openai's api)
    '''
    queryset = VisualArt.objects.all()
    serializer_class = VisualArtOutputSerializer


class MovementInputViewSet(generics.CreateAPIView):
    '''
    METHODS: POST
    Creates user input/prompt instance to send to openai's api
    Calls get_movement_length() function to get user inputted prompt length
    Calls send_movement_prompt() function to connect call openai's api
    Asynch - 1 second delay between calling the 2 functions
    '''
    queryset = Movement.objects.all()
    serializer_class = MovementInputSerializer

    def perform_create(self, serializer):
        movement = serializer.save()
        length = serializer.save()

        length.get_movement_length()
        time.sleep(1)
        movement.send_movement_prompt()


class MovementOutputViewSet(generics.RetrieveAPIView):
    '''
    METHODS: GET
    Retrieves Movement instance from the database (including 'output' which has now been supplied by openai's api)
    '''
    queryset = Movement.objects.all()
    serializer_class = MovementOutputSerializer


class MusicInputViewSet(generics.CreateAPIView):
    '''
    METHODS: POST
    Creates user input/prompt instance to send to openai's api
    Calls get_music_length() function to get user inputted prompt length
    Calls send_music_prompt() function to connect call openai's api
    Asynch - 1 second delay between calling the 2 functions
    '''
    queryset = Music.objects.all()
    serializer_class = MusicInputSerializer

    def perform_create(self, serializer):
        music = serializer.save()
        length = serializer.save()

        length.get_music_length()
        time.sleep(1)
        music.send_music_prompt()


class MusicOutputViewSet(generics.RetrieveAPIView):
    '''
    METHODS: GET
    Retrieves Music instance from the database (including 'output' which has now been supplied by openai's api)
    '''
    queryset = Music.objects.all()
    serializer_class = MusicOutputSerializer
