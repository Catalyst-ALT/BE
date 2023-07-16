from rest_framework import generics, permissions
# from django.shortcuts import render, get_object_or_404
from .models import User, Poem, Prompt
from .serializers import PoemSerializer, ProfileSerializer, PoemOutputSerializer
from catalyst.permissions import IsProfileOwnerOrReadOnly
from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
import openai
import requests
import json


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


class PoemViewSet(generics.CreateAPIView):
    '''
    METHODS: POST
    '''
    queryset = Poem.objects.all()
    serializer_class = PoemSerializer

    def perform_create(self, serializer):
        poem = serializer.save()
        poem.send_prompt()


class PoemOutputViewSet(generics.ListCreateAPIView):
    '''
    METHODS: GET/POST
    '''
    queryset = Poem.objects.all()
    serializer_class = PoemOutputSerializer
