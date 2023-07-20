from rest_framework import generics, permissions
from .models import User, Write, VisualArt, Movement, Music, Note, Welcome, Definition
from .serializers import DefinitionInputSerializer, DefinitionOutputSerializer, WelcomeSerializer, AllPromptsArchiveSerializer, MusicInputSerializer, MusicOutputSerializer, WriteInputSerializer, ProfileSerializer, WriteOutputSerializer, VisualArtInputSerializer, VisualArtOutputSerializer, MovementInputSerializer, MovementOutputSerializer
from catalyst.permissions import IsProfileOwnerOrReadOnly
import time
from rest_framework.response import Response
from rest_framework import status
from drf_multiple_model.views import ObjectMultipleModelAPIView
from rest_framework.serializers import Serializer
from rest_framework import request
from rest_framework.views import APIView
from rest_framework.decorators import action


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
        word = serializer.save()
        length = serializer.save()

        length.get_write_length()
        time.sleep(1)
        word.send_write_prompt()


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


class AllPromptsArchiveViewSet(generics.ListAPIView):
    '''
    METHODS: GET 
    List of all outputs/prompts user has received
    '''
    queryset = User.objects.all()
    serializer_class = AllPromptsArchiveSerializer

    def perform_create(self, serializer):
        serializer.save(writes=self.request.user)
        serializer.save(visual_arts=self.request.user)
        serializer.save(movements=self.request.user)
        serializer.save(music=self.request.user)


class AllWritePromptViewSet(generics.ListAPIView):
    '''
    METHODS: GET
    List all write outputs/prompts user has received
    '''
    queryset = Write.objects.all()
    serializer_class = WriteOutputSerializer


class AllVisualArtPromptViewSet(generics.ListAPIView):
    '''
    METHODS: GET
    List all visual art outputs/prompts user has received
    '''
    queryset = VisualArt.objects.all()
    serializer_class = VisualArtOutputSerializer


class AllMovementPromptViewSet(generics.ListAPIView):
    '''
    METHODS: GET
    List all movement outputs/prompts user has received
    '''
    queryset = Movement.objects.all()
    serializer_class = MovementOutputSerializer


class AllMusicPromptViewSet(generics.ListAPIView):
    '''
    METHODS: GET
    List all music outputs/prompts user has received
    '''
    queryset = Music.objects.all()
    serializer_class = MusicOutputSerializer


# class NoteCreateViewSet(generics.CreateAPIView):
#     '''
#     METHODS: POST
#     Create Note instance
#     '''
#     queryset = Note.objects.all()
#     serializer_class = NoteSerializer


# class NoteRetrieveUpdateDestroyViewSet(generics.RetrieveUpdateDestroyAPIView):
#     '''
#     METHODS: GET, UPDATE, DELETE
#     Retrieve, update, and destroy a note instance
#     '''
#     queryset = Note.objects.all()
#     serializer_class = NoteSerializer


# class NoteFoliosViewSet(generics.ListAPIView):
#     '''
#     METHODS: GET
#     Retrieve list of all user notes
#     '''
#     queryset = Note.objects.all()
#     serializer_class = NoteSerializer


class WelcomeInputViewSet(generics.CreateAPIView):
    querset = Welcome.objects.all()
    serializer_class = WelcomeSerializer

    def perform_create(self, serializer):
        hello = serializer.save()
        hello.send_welcome_prompt()


class WelcomeOutputViewSet(generics.RetrieveAPIView):
    queryset = Welcome.objects.all()
    serializer_class = WelcomeSerializer


class DefinitionInputViewSet(generics.CreateAPIView):
    queryset = Definition.objects.all()
    serializer_class = DefinitionInputSerializer

    def perform_create(self, serializer):
        define = serializer.save()
        define.send_definition_prompt()


class DefinitionOutputViewSet(generics.RetrieveAPIView):
    queryset = Definition.objects.all()
    serializer_class = DefinitionOutputSerializer
