from django.db import models
from django.contrib.auth.models import AbstractUser
import openai
import environ
import time
from django.core.exceptions import ValidationError

ONE_WORD = 'one word'
THREE_WORDS = 'three words'
PROMPT = 'prompt'

LENGTH_CHOICES = [
    (ONE_WORD, 'one word'),
    (THREE_WORDS, 'three words'),
    (PROMPT, 'prompt'),
]


class User(AbstractUser):
    pass

    def __str__(self):
        return self.username


class Note(models.Model):
    text = models.TextField(blank=True)

    def __str__(self):
        return str(self.id)


class Write(models.Model):

    style = models.CharField(max_length=50, blank=True)
    theme = models.CharField(max_length=50, blank=True)
    category = models.CharField(
        max_length=50, blank=True)
    sentiment = models.CharField(
        max_length=50, blank=True)
    emotion = models.CharField(
        max_length=50, blank=True)
    user = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name='writes', blank=True, null=True)
    prompt_length = models.CharField(max_length=50)
    input_length = models.CharField(blank=True, max_length=300)
    output = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    note = models.ForeignKey(to=Note, on_delete=models.CASCADE,
                             related_name='writes_notes', blank=True, null=True)

    class WriteManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().order_by('-date')

    def get_write_length(self):
        if self.prompt_length == 'one word':
            words = "Let the prompt be only 1 word"
        elif self.prompt_length == 'three words':
            words = 'Let the prompt be only 3 words'
        elif self.prompt_length == 'prompt':
            words = "Let the prompt be 20-25 words"

        self.input_length = words
        self.save()

    def send_write_prompt(self):
        write_input = f'Give a writer a prompt for writing with the keywords: {self.theme}, {self.category}, {self.sentiment}, {self.emotion}. {self.input_length}. Do not use the keywords in the prompt. Return only text.'
        env = environ.Env()
        environ.Env.read_env()
        MODEL = "gpt-3.5-turbo"
        openai.api_key = env('OPENAI_API_KEY')
        response = openai.ChatCompletion.create(
            model=MODEL,
            messages=[
                {"role": "system",
                    "content": "You are a helpful assistant"},
                {"role": "user", "content": write_input}
            ],
            temperature=0.5,
        )
        self.output = response['choices'][0]['message']['content']
        self.save()

    def __str__(self):
        return str(self.id)


class VisualArt(models.Model):

    medium = models.CharField(
        max_length=50, blank=True)
    theme = models.CharField(
        max_length=50, blank=True)
    sentiment = models.CharField(
        max_length=50, blank=True)
    emotion = models.CharField(
        max_length=50, blank=True)
    user = user = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name='visual_arts', blank=True, null=True)
    prompt_length = models.CharField(choices=LENGTH_CHOICES)
    input_length = models.CharField(blank=True, max_length=300)
    output = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    note = models.ForeignKey(to=Note, on_delete=models.CASCADE,
                             related_name='visual_art_notes', blank=True, null=True)

    def get_visual_art_length(self):
        if self.prompt_length == 'one word':
            words = "Let the prompt be only 1 word"
        elif self.prompt_length == 'three words':
            words = 'Let the prompt be only 3 words'
        elif self.prompt_length == 'prompt':
            words = "Let the prompt be 20-25 words"

        self.input_length = words
        self.save()

    def send_visual_art_prompt(self):
        visual_art_input = f'Give an artist a {self.medium} prompt with the keywords: {self.theme}, {self.sentiment}, and {self.emotion}. {self.input_length}. Do not use the keywords in the prompt. Return only text.'
        env = environ.Env()
        environ.Env.read_env()
        MODEL = "gpt-3.5-turbo"
        openai.api_key = env('OPENAI_API_KEY')
        response = openai.ChatCompletion.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": visual_art_input}
            ],
            temperature=0.5,
        )
        self.output = response['choices'][0]['message']['content']
        self.save()

    def __str__(self):
        return str(self.id)


class Movement(models.Model):

    theme = models.CharField(max_length=50, blank=True)
    somatic = models.CharField(
        max_length=50, blank=True)
    sentiment = models.CharField(
        max_length=50, blank=True)
    emotion = models.CharField(
        max_length=50, blank=True)
    user = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name='movements', blank=True, null=True)
    prompt_length = models.CharField(choices=LENGTH_CHOICES)
    input_length = models.CharField(blank=True, max_length=300)
    output = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    note = models.ForeignKey(to=Note, on_delete=models.CASCADE,
                             related_name='movement_notes', blank=True, null=True)

    def get_movement_length(self):
        if self.prompt_length == 'one word':
            words = "Let the prompt be only 1 word"
        elif self.prompt_length == 'three words':
            words = 'Let the prompt be only 3 words'
        elif self.prompt_length == 'prompt':
            words = "Let the prompt be 20-25 words"

        self.input_length = words
        self.save()

    def send_movement_prompt(self):
        movement_input = f'Give a movement artist a prompt with the keywords: {self.theme}, {self.somatic}, {self.emotion}, {self.sentiment}. {self.input_length}. Do not use the keywords in the prompt. Return only text.'
        env = environ.Env()
        environ.Env.read_env()
        MODEL = "gpt-3.5-turbo"
        openai.api_key = env('OPENAI_API_KEY')
        response = openai.ChatCompletion.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": movement_input}
            ],
            temperature=0.5,
        )
        self.output = response['choices'][0]['message']['content']
        self.save()

    def __str__(self):
        return str(self.id)


class Music(models.Model):

    exploration = models.CharField(
        max_length=50, blank=True)
    concept = models.CharField(
        max_length=50, blank=True)
    element = models.CharField(
        max_length=50, blank=True)
    emotion = models.CharField(
        max_length=50, blank=True)
    user = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name='music', blank=True, null=True)
    prompt_length = models.CharField(choices=LENGTH_CHOICES)
    input_length = models.CharField(blank=True, max_length=300)
    output = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    note = models.ForeignKey(to=Note, on_delete=models.CASCADE,
                             related_name='music_notes', blank=True, null=True)

    def get_music_length(self):
        if self.prompt_length == 'one word':
            words = "Let the prompt be only 1 word"
        elif self.prompt_length == 'three words':
            words = 'Let the prompt be only 3 words'
        elif self.prompt_length == 'prompt':
            words = "Let the prompt be 20-25 words"

        self.input_length = words
        self.save()

    def send_music_prompt(self):
        music_input = f'Give a musician a prompt for music with the keywords: "{self.exploration}", "{self.concept}", "{self.emotion}", "{self.element}". {self.input_length}. Do not use the keywords in the prompt. Return only text.'
        env = environ.Env()
        environ.Env.read_env()
        MODEL = "gpt-3.5-turbo"
        openai.api_key = env('OPENAI_API_KEY')
        response = openai.ChatCompletion.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": music_input}
            ],
            temperature=0.5,
        )
        self.output = response['choices'][0]['message']['content']
        self.save()

    def __str__(self):
        return str(self.id)
