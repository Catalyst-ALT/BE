from django.db import models
from django.contrib.auth.models import AbstractUser
import openai
import requests
import json
import environ


class User(AbstractUser):
    pass

    def __str__(self):
        return self.username


class Poem(models.Model):

    ASSOCIATION = 'association'
    EMOTION = 'emotion'
    EXPLORATION = 'exploration'
    HISTORICAL_CULTURAL = 'historical/cultural'
    CONCEPTUAL = 'conceptual'
    THEME_CHOICES = [
        (ASSOCIATION, 'association'),
        (EMOTION, 'emotion'),
        (EXPLORATION, 'exploration'),
        (HISTORICAL_CULTURAL, 'historial/cultural'),
        (CONCEPTUAL, 'conceptual'),
    ]

    RELATIONSHIPS_AND_LOVE = 'relationships and love'
    NATURE_AND_ENVIRONMENT = 'nature and environment'
    PERSONAL_GROWTH_AND_RELATIONSHIP = 'personal growth and relationship'
    SOCIAL_ISSUES_AND_ADVOCACY = 'social issues and advocacy'
    MYTHOLOGY_AND_FOLKLORE = 'mythology and folklore'
    SURREALISM_AND_DREAMS = 'surrealism_and_dreams'
    HISTORY = 'history'
    IDENTITY_AND_DIVERSITY = 'identity and diversity'
    IMAGERY_AND_SYMBOLISM = 'imagery and symbolism'
    CATEGORY_CHOICES = [
        (RELATIONSHIPS_AND_LOVE, 'relationships and love'),
        (NATURE_AND_ENVIRONMENT, 'natural and environment'),
        (PERSONAL_GROWTH_AND_RELATIONSHIP, 'personal growth and relationship'),
        (SOCIAL_ISSUES_AND_ADVOCACY, 'social issues and advocacy'),
        (MYTHOLOGY_AND_FOLKLORE, 'mythology and folklore'),
        (SURREALISM_AND_DREAMS, 'surrealism and dreams'),
        (HISTORY, 'history'),
        (IDENTITY_AND_DIVERSITY, 'identity and diversity'),
        (IMAGERY_AND_SYMBOLISM, 'imagery and symbolism'),
    ]

    HARMONY = 'harmony'
    RESILIENCE = 'resilience'
    FRAGILITY = 'fragility'
    MAJESTY = 'majesty'
    SERENITY = 'serenity'
    WONDER = 'wonder'
    TRANSIENCE = 'transience'
    CONNECTION = 'connection'
    SOLITUDE = 'solitude'
    RENEWAL = 'renewal'
    SENTIMENT_CHOICES = [
        (HARMONY, 'harmony'),
        (RESILIENCE, 'resilience'),
        (FRAGILITY, 'fragility'),
        (MAJESTY, 'majesty'),
        (SERENITY, 'serenity'),
        (WONDER, 'wonder'),
        (TRANSIENCE, 'transience'),
        (CONNECTION, 'connection'),
        (SOLITUDE, 'solitude'),
        (RENEWAL, 'renewal'),
    ]

    JOY = 'joy'
    COURAGE = 'courage'
    MELANCHOLY = 'melancholy'
    EUPHORIA = 'euphoria'
    LONGING = 'longing'
    HOPE = 'hope'
    AWE = 'awe'
    BLISS = 'bliss'
    ANGUISH = 'anguish'
    GRIEF = 'grief'
    EMOTION_CHOICES = [
        (JOY, 'joy'),
        (COURAGE, 'courage'),
        (MELANCHOLY, 'melancholy'),
        (EUPHORIA, 'euphoria'),
        (LONGING, 'longing'),
        (HOPE, 'hope'),
        (AWE, 'awe'),
        (BLISS, 'bliss'),
        (ANGUISH, 'anguish'),
        (GRIEF, 'grief'),
    ]

    theme = models.CharField(max_length=50, default='', choices=THEME_CHOICES)
    category = models.CharField(
        max_length=50, default='', choices=CATEGORY_CHOICES)
    sentiment = models.CharField(
        max_length=50, default='', choices=SENTIMENT_CHOICES)
    emotion = models.CharField(
        max_length=50, default='', choices=EMOTION_CHOICES)
    input_sentiment = models.CharField(
        max_length=50, null=True, blank=True)
    input_emotion = models.CharField(
        max_length=50, null=True, blank=True)
    user = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name='poems', blank=True, null=True)
    output = models.TextField(blank=True)

    def send_prompt(self):
        '''
        Sends POST request to openai's API with user choices wrapped in a prompt with parameters for the gpt model
        Uses key/value pairing to access the gpt model's output (key='content')
        Saves chat gpt response to output field on Poem model
        temperature 1.5 = very creative
        '''
        input = f'Give a poet a prompt for writing poetry with the keywords: {self.theme}, {self.category}, {self.sentiment}, {self.emotion}. Let the prompt be 20-25 words. Do not use the keywords in the prompt. Return only text'
        env = environ.Env()
        environ.Env.read_env()
        MODEL = "gpt-3.5-turbo"
        openai.api_key = env('OPENAI_API_KEY')
        response = openai.ChatCompletion.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": input}
            ],
            temperature=1.5,
        )
        self.output = response['choices'][0]['message']['content']
        self.save()

    def __str__(self):
        return str(self.id)


class Prompt(models.Model):
    poem = models.ForeignKey(
        to=Poem, on_delete=models.CASCADE, related_name='prompts', blank=True, null=True)

    def __str__(self):
        return str(self.id)
