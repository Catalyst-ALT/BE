from rest_framework import generics, permissions
# from django.shortcuts import render
from .models import User, Poem
from .serializers import PoemSerializer
# import requests
# import openai
# import environ
# import os
# from django.conf import Settings
# from django.http import HttpResponse
# from django.http import JsonResponse
# from rest_framework.decorators import api_view


# class ProfileViewSet(generics.RetrieveUpdateDestroyAPIView):
#     '''
#     Methods: GET, PATCH, DELETE
#     PATCH and DELETE methods only able to be performed by profile owner
#     '''
#     queryset = User.objects.all()
#     serializer_class = ProfileSerializer
#     lookup_field = "username"
#     permission_classes = [
#         permissions.IsAuthenticatedOrReadOnly, IsProfileOwnerOrReadOnly]


class PoemViewSet(generics.CreateAPIView):
    '''
    METHODS: POST
    '''
    queryset = Poem.objects.all()
    serializer_class = PoemSerializer
