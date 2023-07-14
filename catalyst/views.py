from rest_framework import generics, permissions
from django.shortcuts import render
from .models import User, Poem
from .serializers import PoemSerializer
# Create your views here.


class PoemViewSet(generics.CreateAPIView):
    '''
    METHODS: POST
    '''
    queryset = Poem.objects.all()
    serializer_class = PoemSerializer
