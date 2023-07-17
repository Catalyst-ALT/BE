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


class Write(models.Model):

    ASSOCIATION = 'association'
    EMOTION = 'emotion'
    EXPLORATION = 'exploration'
    HISTORICAL_CULTURAL = 'historical and cultural'
    CONCEPTUAL = 'conceptual'
    THEME_CHOICES = [
        (ASSOCIATION, 'association'),
        (EMOTION, 'emotion'),
        (EXPLORATION, 'exploration'),
        (HISTORICAL_CULTURAL, 'historical and cultural'),
        (CONCEPTUAL, 'conceptual'),
    ]

    RELATIONSHIPS_AND_LOVE = 'relationships and love'
    NATURE_AND_ENVIRONMENT = 'nature and environment'
    PERSONAL_GROWTH_AND_REFLECTION = 'personal growth and reflection'
    SOCIAL_ISSUES_AND_ADVOCACY = 'social issues and advocacy'
    MYTHOLOGY_AND_FOLKLORE = 'mythology and folklore'
    SURREALISM_AND_DREAMS = 'surrealism and dreams'
    HISTORY = 'history'
    IDENTITY_AND_DIVERSITY = 'identity and diversity'
    IMAGERY_AND_SYMBOLISM = 'imagery and symbolism'
    CATEGORY_CHOICES = [
        (RELATIONSHIPS_AND_LOVE, 'relationships and love'),
        (NATURE_AND_ENVIRONMENT, 'natural and environment'),
        (PERSONAL_GROWTH_AND_REFLECTION, 'personal growth and REFLECTION'),
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
    user = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name='poems', blank=True, null=True)
    output = models.TextField(blank=True)

    def send_write_prompt(self):
        '''
        Sends POST request to openai's API with user choices wrapped in a prompt with parameters for the gpt model
        Uses key/value pairing to access the gpt model's output (key='content')
        Saves chat gpt response to output field on Poem model
        temperature 1.5 = very creative
        '''
        write_input = f'Give a poet a prompt for writing poetry with the keywords: {self.theme}, {self.category}, {self.sentiment}, {self.emotion}. Let the prompt be 20-25 words. Do not use the keywords in the prompt. Return only text.'
        env = environ.Env()
        environ.Env.read_env()
        MODEL = "gpt-3.5-turbo"
        openai.api_key = env('OPENAI_API_KEY')
        response = openai.ChatCompletion.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": write_input}
            ],
            temperature=1.5,
        )
        self.output = response['choices'][0]['message']['content']
        self.save()

    def __str__(self):
        return str(self.id)


class VisualArt(models.Model):
    PAINTING = 'painting'
    DRAWING = 'drawing'
    SCULPTURE = 'sculpture'
    PRINTMAKING = 'printmaking'
    DIGITAL_ART = 'digital art'
    ILLUSTRATION = 'illustration'
    PHOTOGRAPHY = 'photography'
    MIXED_MEDIA = 'mixed media'
    MEDIUM_CHOICES = [
        (PAINTING, 'painting'),
        (DRAWING, 'drawing'),
        (SCULPTURE, 'sculpture'),
        (PRINTMAKING, 'printmaking'),
        (DIGITAL_ART, 'digital art'),
        (ILLUSTRATION, 'illustration'),
        (PHOTOGRAPHY, 'photography'),
        (MIXED_MEDIA, 'mixed media'),
    ]

    PORTRAITURE = 'portraiture'
    TEXTURE = 'texture'
    SYMBOLISM = 'symbolism'
    NATURE_AND_LANDSCAPES = 'nature and landscapes'
    STORYTELLING_AND_NARRATIVE = 'storytelling and narrative'
    ABSTRACTION = 'abstraction'
    SOCIAL_COMMENTARY = 'social commentary'
    LIGHT_AND_SHADOW = 'light and shadow'
    COLLAGE_AND_MIXED_MEDIA = 'collage and mixed media'
    EXPERIMENTATION = 'experimentation'
    CONCEPTUAL = 'conceptual'
    MINIMALISM = 'minimalism'
    MOVEMENT_AND_ENERGY = "movement and energy"
    HARMONY_AND_BALANCE = 'harmony and balance'
    THEME_CHOICES = [
        (PORTRAITURE, 'portraiture'),
        (TEXTURE, 'texture'),
        (SYMBOLISM, 'symbolism'),
        (NATURE_AND_LANDSCAPES, 'nature and landscapes'),
        (STORYTELLING_AND_NARRATIVE, 'storytelling and narrative'),
        (ABSTRACTION, 'abstraction'),
        (SOCIAL_COMMENTARY, 'social commentary'),
        (LIGHT_AND_SHADOW, 'light and shadow'),
        (COLLAGE_AND_MIXED_MEDIA, 'collage and mixed media'),
        (EXPERIMENTATION, 'experimentation'),
        (CONCEPTUAL, 'conceptual'),
        (MINIMALISM, 'minimalism'),
        (MOVEMENT_AND_ENERGY, 'movement and energy'),
        (HARMONY_AND_BALANCE, 'harmony and balance')
    ]

    HARMONY = 'harmony'
    SERENITY = 'serenity'
    SOLITUDE = 'solitude'
    RESILIENCE = 'resilience'
    WONDER = 'wonder'
    RENEWAL = 'renewal'
    FRAGILITY = 'fragility'
    MAJESTY = 'majesty'
    TRANSIENCE = 'transience'
    CONNECTION = 'connection'
    SENTIMENT_CHOICES = [
        (HARMONY, 'harmony'),
        (SERENITY, 'serenity'),
        (SOLITUDE, 'solitude'),
        (RESILIENCE, 'resilience'),
        (WONDER, 'wonder'),
        (RENEWAL, 'renewal'),
        (FRAGILITY, 'fragility'),
        (MAJESTY, 'majesty'),
        (TRANSIENCE, 'transience'),
        (CONNECTION, 'connection')
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
        (GRIEF, 'grief')
    ]

    medium = models.CharField(
        max_length=50, default='', choices=MEDIUM_CHOICES)
    theme = models.CharField(
        max_length=50, default='', choices=THEME_CHOICES)
    sentiment = models.CharField(
        max_length=50, default='', choices=SENTIMENT_CHOICES)
    emotion = models.CharField(
        max_length=50, default='', choices=EMOTION_CHOICES)
    temperature = models.IntegerField(default=1)
    user = user = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name='visualarts', blank=True, null=True)
    output = models.TextField(blank=True)

    def send_visual_art_prompt(self):
        '''
        Sends POST request to openai's API with user choices wrapped in a prompt with parameters for the gpt model
        Uses key/value pairing to access the gpt model's output (key='content')
        Saves chat gpt response to output field on Poem model
        '''
        visual_art_input = f'Give an artist a {self.medium} prompt with the keywords: {self.theme}, {self.sentiment}, and {self.emotion}. Let the prompt be 20-25 words. Do not use the keywords in the prompt. Return only text.'
        temperature = self.temperature
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
            temperature=temperature,
        )
        self.output = response['choices'][0]['message']['content']
        self.save()

    def __str__(self):
        return str(self.id)


class Movement(models.Model):
    SPATIAL_AWARENESS = 'spatial awareness'
    EMOTIONAL_LANDSCAPE = 'emotional landscape'
    EXPRESSIVE_GESTURES = 'expressive gestures'
    RHYTHM_AND_FLOW = 'rhythm and flow'
    ABSTRACT_AND_EXPRESSION = 'abstract and expression'
    PERSONAL_NARRATIVES = 'personal narratives'
    NATURE_IN_MOTION = 'nature in motion'
    CULTURAL_FUSION = 'cultural fusion'
    HUMAN_CONNECTION = 'human connection'
    THEME_CHOICES = [
        (SPATIAL_AWARENESS, 'spatial awareness'),
        (EMOTIONAL_LANDSCAPE, 'emotional landscape'),
        (EXPRESSIVE_GESTURES, 'expressive gestures'),
        (RHYTHM_AND_FLOW, 'rhythm and flow'),
        (ABSTRACT_AND_EXPRESSION, 'abstract and expression'),
        (PERSONAL_NARRATIVES, 'personal narratives'),
        (NATURE_IN_MOTION, 'nature in motion'),
        (CULTURAL_FUSION, 'cultural fusion'),
        (HUMAN_CONNECTION, 'human connection')
    ]

    EMBODIED_AWARENESS = 'embodied awareness'
    BREATH_AND_MOVEMENT = 'breath and movement'
    BODY_MIND_CONNECTION = 'body-mind connection'
    ANATOMY = 'anatomy'
    AUTHENTIC_MOVEMENT = 'authentic movement'
    GROUNDING_AND_CENTERING = 'grounding and centering'
    BODY_MAPPING = 'body mapping'
    MINDFUL_MOVEMENT = 'mindful movement'
    SOMATIC_IMAGINATION = 'somatic imagination'
    SOMATIC_CHOICES = [
        (EMBODIED_AWARENESS, 'embodied awareness'),
        (BREATH_AND_MOVEMENT, 'breath and movement'),
        (BODY_MIND_CONNECTION, 'body-mind connection'),
        (ANATOMY, 'anatomy'),
        (AUTHENTIC_MOVEMENT, 'authentic movement'),
        (GROUNDING_AND_CENTERING, 'grounding and centering'),
        (BODY_MAPPING, 'body mapping'),
        (MINDFUL_MOVEMENT, 'mindful movement'),
        (SOMATIC_IMAGINATION, 'somatic imagination')
    ]

    HARMONY = 'harmony'
    SERENITY = 'serenity'
    SOLITUDE = 'solitude'
    RESILIENCE = 'resilience'
    WONDER = 'wonder'
    RENEWAL = 'renewal'
    FRAGILITY = 'fragility'
    MAJESTY = 'majesty'
    TRANSIENCE = 'transience'
    CONNECTION = 'connection'
    SENTIMENT_CHOICES = [
        (HARMONY, 'harmony'),
        (SERENITY, 'serenity'),
        (SOLITUDE, 'solitude'),
        (RESILIENCE, 'resilience'),
        (WONDER, 'wonder'),
        (RENEWAL, 'renewal'),
        (FRAGILITY, 'fragility'),
        (MAJESTY, 'majesty'),
        (TRANSIENCE, 'transience'),
        (CONNECTION, 'connection')
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
        (GRIEF, 'grief')
    ]
    theme = models.CharField(max_length=50, default='', choices=THEME_CHOICES)
    somatic = models.CharField(
        max_length=50, default='', choices=SOMATIC_CHOICES)
    sentiment = models.CharField(
        max_length=50, default='', choices=SENTIMENT_CHOICES)
    emotion = models.CharField(
        max_length=50, default='', choices=EMOTION_CHOICES)
    temperature = models.IntegerField(default=1)
    user = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name='movements', blank=True, null=True)
    output = models.TextField(blank=True)

    def send_movement_prompt(self):
        '''
        Sends POST request to openai's API with user choices wrapped in a prompt with parameters for the gpt model
        Uses key/value pairing to access the gpt model's output (key='content')
        Saves chat gpt response to output field on Poem model
        '''
        movement_input = f'Give a movement artist a prompt with the keywords: {self.theme}, {self.somatic}, {self.emotion}, {self.sentiment}. Let the prompt be 20-25 words. Do not use the keywords in the prompt. Return only text.'
        temperature = self.temperature
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
            temperature=temperature,
        )
        self.output = response['choices'][0]['message']['content']
        self.save()

    def __str__(self):
        return str(self.id)
