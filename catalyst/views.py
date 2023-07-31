from rest_framework import generics, permissions
from drf_multiple_model.views import ObjectMultipleModelAPIView
from catalyst.permissions import (
    IsProfileOwnerOrReadOnly,
    IsWriteOwnerOrReadOnly,
    IsMusicOwnerOrReadOnly,
    IsVisualArtOwnerOrReadOnly,
    IsMovementOwnerOrReadOnly,
    IsUserMediaOrReadOnly,
)
import time
from .models import (
    User,
    Write,
    VisualArt,
    Movement,
    Music,
    Welcome,
    Definition,
)

from .serializers import (
    DefinitionInputSerializer,
    DefinitionOutputSerializer,
    WelcomeSerializer,
    AllMediumsSerializer,
    MusicInputSerializer,
    MusicOutputSerializer,
    WriteInputSerializer,
    ProfileSerializer,
    WriteOutputSerializer,
    VisualArtInputSerializer,
    VisualArtOutputSerializer,
    MovementInputSerializer,
    MovementOutputSerializer,
)


class ProfileViewSet(generics.RetrieveUpdateDestroyAPIView):
    '''
    Methods: GET, PATCH, DELETE
    PATCH and DELETE methods only able to be performed by profile owner
    '''
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = "username"
    # permission_classes = [
    #     permissions.IsAuthenticatedOrReadOnly, IsProfileOwnerOrReadOnly]


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
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        word = serializer.save()
        length = serializer.save()
        # previous = serializer.save()
        # new = serializer.save()

        length.get_write_length()
        time.sleep(1)
        word.send_write_prompt()
        # time.sleep(7)
        # previous.get_previous_output()
        # time.sleep(1)
        # new.create_or_update_instance()


class WriteOutputViewSet(generics.RetrieveUpdateDestroyAPIView):
    '''
    METHODS: GET, PATCH, DELETE
    '''
    queryset = Write.objects.all()
    serializer_class = WriteOutputSerializer
    # def get_queryset(self):
    #     return self.request.user.writes
    # serializer_class = WriteOutputSerializer
    # permission_classes = [permissions.IsAuthenticated, IsWriteOwnerOrReadOnly]


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
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        visualart = serializer.save()
        length = serializer.save()

        length.get_visual_art_length()
        time.sleep(1)
        visualart.send_visual_art_prompt()


class VisualArtOutputViewSet(generics.RetrieveUpdateDestroyAPIView):
    '''
    METHODS: GET, PATCH, DELETE
    '''
    queryset = VisualArt.objects.all()
    serializer_class = VisualArtOutputSerializer
    # def get_queryset(self):
    #     return self.request.user.visual_arts
    # serializer_class = VisualArtOutputSerializer
    # permission_classes = [permissions.IsAuthenticated, IsVisualArtOwnerOrReadOnly]


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
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        movement = serializer.save()
        length = serializer.save()

        length.get_movement_length()
        time.sleep(1)
        movement.send_movement_prompt()


class MovementOutputViewSet(generics.RetrieveUpdateDestroyAPIView):
    '''
    METHODS: GET, PATCH, DELETE
    '''
    queryset = Movement.objects.all()
    serializer_class = MovementOutputSerializer

    # def get_queryset(self):
    #     return self.request.user.movements
    # serializer_class = MovementOutputSerializer
    # permission_classes = [permissions.IsAuthenticated, IsMovementOwnerOrReadOnly]


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
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        music = serializer.save()
        length = serializer.save()

        length.get_music_length()
        time.sleep(1)
        music.send_music_prompt()


class MusicOutputViewSet(generics.RetrieveUpdateDestroyAPIView):
    '''
    METHODS: GET, PATCH, DELETE
    '''
    queryset = Music.objects.all()
    serializer_class = MusicOutputSerializer

    # def get_queryset(self):
    #     return self.request.user.music
    # serializer_class = MusicOutputSerializer
    # permission_classes = [permissions.IsAuthenticated, IsMusicOwnerOrReadOnly]


class AllMediumsViewSet(generics.ListAPIView):
    '''
    METHODS: GET
    List of all user mediums (Write, VisualArt,
    Movement, Music) and their attributes (prompts, notes, id, etc) 
    '''
    queryset = User.objects.all()
    serializer_class = AllMediumsSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(writes=self.request.user)
        serializer.save(visual_arts=self.request.user)
        serializer.save(movements=self.request.user)
        serializer.save(music=self.request.user)


class AllWriteViewSet(generics.ListAPIView):
    '''
    METHODS: GET
    List all write instances including opeanai output and note
    '''
    queryset = Write.objects.filter(
        is_deleted=False)
    serializer_class = WriteOutputSerializer
    # def get_queryset(self):
    #     return self.request.user.writes
    # serializer_class = WriteOutputSerializer
    # permission_classes = [permissions.IsAuthenticated, IsWriteOwnerOrReadOnly]


class AllVisualArtViewSet(generics.ListAPIView):
    '''
    METHODS: GET
    List all visual art instances including opeanai output and note
    '''
    queryset = VisualArt.objects.filter(
        is_deleted=False)
    serializer_class = VisualArtOutputSerializer

    # def get_queryset(self):
    #     return self.request.user.visual_arts
    # serializer_class = VisualArtOutputSerializer
    # permission_classes = [permissions.IsAuthenticated, IsVisualArtOwnerOrReadOnly]


class AllMovementViewSet(generics.ListAPIView):
    '''
    METHODS: GET
    List all movement instances including opeanai output and note
    '''
    queryset = Movement.objects.filter(
        is_deleted=False)
    serializer_class = MovementOutputSerializer

    # def get_queryset(self):
    #     return self.request.user.movements
    # serializer_class = MovementOutputSerializer
    # permission_classes = [permissions.IsAuthenticated, IsMovementOwnerOrReadOnly]


class AllMusicViewSet(generics.ListAPIView):
    '''
    METHODS: GET
    List all movement instances including opeanai output and note
    '''
    queryset = Music.objects.filter(
        is_deleted=False)
    serializer_class = MusicOutputSerializer

    # def get_queryset(self):
    #     return self.request.user.music
    # serializer_class = MusicOutputSerializer
    # permission_classes = [permissions.IsAuthenticated, IsMusicOwnerOrReadOnly]


class SavePromptViewSet(ObjectMultipleModelAPIView):
    '''
    METHODS: GET
    Retrieves list of all prompts saved by user
    '''
    querylist = [
        {'queryset': Write.objects.filter(
            save_prompt=True), 'serializer_class': WriteOutputSerializer},
        {'queryset': VisualArt.objects.filter(
            save_prompt=True), 'serializer_class': VisualArtOutputSerializer},
        {'queryset': Movement.objects.filter(
            save_prompt=True), 'serializer_class': MovementOutputSerializer},
        {'queryset': Music.objects.filter(
            save_prompt=True), 'serializer_class': MusicOutputSerializer},
    ]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AllNotesViewSet(ObjectMultipleModelAPIView):
    '''
    METHODS: GET
    Retrieves list of all notes written by user
    '''
    querylist = [
        {'queryset': Write.objects.exclude(
            note__exact=''), 'serializer_class': WriteOutputSerializer},
        {'queryset': VisualArt.objects.exclude(
            note__exact=''), 'serializer_class': VisualArtOutputSerializer},
        {'queryset': Movement.objects.exclude(
            note__exact=''), 'serializer_class': MovementOutputSerializer},
        {'queryset': Music.objects.exclude(
            note__exact=''), 'serializer_class': MusicOutputSerializer},
    ]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class WelcomeInputViewSet(generics.CreateAPIView):
    '''
    METHODS: POST
    Creates welcome instance
    '''
    querset = Welcome.objects.all()
    serializer_class = WelcomeSerializer

    def perform_create(self, serializer):
        hello = serializer.save()
        hello.send_welcome_prompt()


class WelcomeOutputViewSet(generics.RetrieveAPIView):
    '''
    METHODS: GET
    Retrieves openai generated welcome message
    '''
    queryset = Welcome.objects.all()
    serializer_class = WelcomeSerializer


class DefinitionInputViewSet(generics.CreateAPIView):
    '''
    METHODS: POST
    Creates definition instance based off user input of word 
    to be defined
    '''
    queryset = Definition.objects.all()
    serializer_class = DefinitionInputSerializer

    def perform_create(self, serializer):
        define = serializer.save()
        syno = serializer.save()
        anto = serializer.save()
        sent = serializer.save()
        funny = serializer.save()
        colour = serializer.save()
        hex_num = serializer.save()

        define.send_definition_prompt()
        syno.send_synonym_prompt()
        anto.send_antonym_prompt()
        sent.send_sentence_prompt()
        funny.send_joke_prompt()
        colour.send_color_prompt()
        hex_num.send_color_prompt()


class DefinitionOutputViewSet(generics.RetrieveAPIView):
    '''
    METHODS: GET
    Retrieves definition instance/openai generated fields
    (definition, color, synonym, antonym, sentence, joke)
    '''
    queryset = Definition.objects.all()
    serializer_class = DefinitionOutputSerializer
