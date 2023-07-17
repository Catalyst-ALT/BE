from rest_framework import generics, permissions
# from django.shortcuts import render, get_object_or_404
from .models import User, Poem, Prompt, VisualArt
from .serializers import PoemInputSerializer, ProfileSerializer, PoemOutputSerializer, VisualArtInputSerializer, VisualArtOutputSerializer
from catalyst.permissions import IsProfileOwnerOrReadOnly
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# import openai
# import requests
# import json


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


class PoemInputViewSet(generics.CreateAPIView):
    '''
    METHODS: POST
    Creates user input/prompt instance to send to openai's api
    Calls send_prompt() function to connect via a post request with openai's api
    '''
    queryset = Poem.objects.all()
    serializer_class = PoemInputSerializer

    def perform_create(self, serializer):
        poem = serializer.save()
        poem.send_prompt()


class PoemOutputViewSet(generics.RetrieveAPIView):
    '''
    METHODS: GET
    Retrieves Poem instance from the database (including 'output' which has now been supplied by openai's api)
    '''
    queryset = Poem.objects.all()
    serializer_class = PoemOutputSerializer


class VisualArtInputViewSet(generics.CreateAPIView):
    '''
    METHODS: POST
    Creates user input/prompt instance to send to openai's api
    Calls send_prompt() function to connect via a post request with openai's api
    '''
    queryset = VisualArt.objects.all()
    serializer_class = VisualArtInputSerializer

    def perform_create(self, serializer):
        visualart = serializer.save()
        visualart.send_visual_art_prompt()


class VisualArtOutputViewSet(generics.RetrieveAPIView):
    '''
    METHODS: GET
    Retrieves Poem instance from the database (including 'output' which has now been supplied by openai's api)
    '''
    queryset = VisualArt.objects.all()
    serializer_class = VisualArtOutputSerializer
