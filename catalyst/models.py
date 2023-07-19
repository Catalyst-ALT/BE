from django.db import models
from django.contrib.auth.models import AbstractUser
import openai
import environ
import time


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

    STREAM_OF_CONCIOUSNESS = 'stream of conciousness'
    TIME = 'time'
    CHARACTER_DEVELOPMENT = 'character development'
    POETRY = 'poetry'
    WORD_PLAY = 'word play'
    STORY_STARTER = 'story starter'
    IMAGE = 'image'
    STORYTELLING_THROUGH_OBJECTS = 'storytelling through objects'
    FLASH = 'flash'
    POINT_OF_VIEW_SHIFT = 'point of view shift'
    MEMOIR = 'memoir'
    DIALOGUE = 'dialogue'
    STYLE_CHOICES = [
        (STREAM_OF_CONCIOUSNESS, 'stream of consciousness'),
        (TIME, 'time'),
        (CHARACTER_DEVELOPMENT, 'character development'),
        (POETRY, 'poetry'),
        (WORD_PLAY, 'word play'),
        (STORY_STARTER, 'story starter'),
        (IMAGE, 'image'),
        (STORYTELLING_THROUGH_OBJECTS, 'storytelling through objects'),
        (FLASH, 'flash'),
        (POINT_OF_VIEW_SHIFT, 'point of view shift'),
        (MEMOIR, 'memoir'),
        (DIALOGUE, 'dialogue')
    ]

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
    style = models.CharField(max_length=50, default='', choices=STYLE_CHOICES)
    theme = models.CharField(max_length=50, default='', choices=THEME_CHOICES)
    category = models.CharField(
        max_length=50, default='', choices=CATEGORY_CHOICES)
    sentiment = models.CharField(
        max_length=50, default='', choices=SENTIMENT_CHOICES)
    emotion = models.CharField(
        max_length=50, default='', choices=EMOTION_CHOICES)
    temperature = models.IntegerField(default=1)
    user = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name='writes', blank=True, null=True)
    prompt_length = models.CharField(choices=LENGTH_CHOICES)
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
        input_temperature = self.temperature
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
            temperature=input_temperature,
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
    temperature = models.FloatField(default=0.8)
    user = user = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name='visual_arts', blank=True, null=True)
    prompt_length = models.CharField(choices=LENGTH_CHOICES)
    input_length = models.CharField(blank=True, max_length=300)
    output = models.TextField(blank=True)

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
        input_temperature = self.temperature
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
            temperature=input_temperature,
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
    temperature = models.FloatField(default=0.8)
    user = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name='movements', blank=True, null=True)
    prompt_length = models.CharField(choices=LENGTH_CHOICES)
    input_length = models.CharField(blank=True, max_length=300)
    output = models.TextField(blank=True)

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
        input_temperature = self.temperature
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
            temperature=input_temperature,
        )
        self.output = response['choices'][0]['message']['content']
        self.save()

    def __str__(self):
        return str(self.id)


class Music(models.Model):

    MOOD_BASED_COMPOSITION = 'mood-based composition'
    GENRE_FUSION = 'genre fusion'
    MUSICAL_STORYTELLING = 'musical storytelling'
    NATURE_SOUNDSCAPE = 'nature soundscape'
    RHYTHMIC_EXPLORATION = 'rhythmic exploration'
    COLLABORATIVE_COMPOSITION = 'collaborative composition'
    MINIMALISM = 'minimalism'
    MASHUP_OR_REMIX = 'mashup or remix'
    MUSIC_FOR_VISUALS = 'music for visuals'
    CINEMATIC_SCORE = 'cinematic score'
    MUSICAL_HAIKU = 'musical haiku'
    ONE_NOTE_CHALLENGE = 'one-note challenge'
    INCORPORATE_UNCONVENTIONAL_INSTRUMENTS = 'incorporate unconventional instruments'
    MUSIC_INSPIRED_BY_ART = 'music inspired by art'
    MUSICAL_TIME_TRAVEL = 'musical time travel'

    EXPLORATION_CHOICES = [
        (MOOD_BASED_COMPOSITION, 'mood-based composition'),
        (GENRE_FUSION, 'genre fusion'),
        (MUSICAL_STORYTELLING, 'musical storytelling'),
        (NATURE_SOUNDSCAPE, 'nature soundscape'),
        (RHYTHMIC_EXPLORATION, 'rhythmic exploration'),
        (COLLABORATIVE_COMPOSITION, 'collaborative composition'),
        (MINIMALISM, 'minimalism'),
        (MASHUP_OR_REMIX, 'mashup or remix'),
        (MUSIC_FOR_VISUALS, 'music for visuals'),
        (CINEMATIC_SCORE, 'cinematic score'),
        (MUSICAL_HAIKU, 'musical haiku'),
        (ONE_NOTE_CHALLENGE, 'one-note challenge'),
        (INCORPORATE_UNCONVENTIONAL_INSTRUMENTS,
         'incorporate unconventional instruments'),
        (MUSIC_INSPIRED_BY_ART, 'music inspired by art'),
        (MUSICAL_TIME_TRAVEL, 'musical time travel')
    ]

    DYNAMICS = 'dynamics'
    TEMPO = 'tempo'
    TIMBRE = 'timbre'
    MELODY = 'melody'
    RHYTHM = 'rhythm'
    TEXTURE = 'texture'
    FORM = 'form'
    EXPRESSION = 'expression'
    PITCH = 'pitch'
    NOTATION = 'notation'

    CONCEPT_CHOICES = [
        (DYNAMICS, 'dynamics'),
        (TEMPO, 'tempo'),
        (TIMBRE, 'timbre'),
        (MELODY, 'melody'),
        (RHYTHM, 'rhythm'),
        (TEXTURE, 'texture'),
        (FORM, 'form'),
        (EXPRESSION, 'expression'),
        (PITCH, 'pitch'),
        (NOTATION, 'notation'),
    ]

    FIRE = 'fire'
    WATER = 'water'
    EARTH = 'earth'
    AIR = 'air'
    LIGHT = 'light'
    DARKNESS = 'darkness'
    SOUND = 'sound'
    MOVEMENT = 'movement'
    TIME = 'time'
    SPACE = 'space'

    ELEMENT_CHOICES = [
        (FIRE, 'fire'),
        (WATER, 'water'),
        (EARTH, 'earth'),
        (AIR, 'air'),
        (LIGHT, 'light'),
        (DARKNESS, 'darkness'),
        (SOUND, 'sound'),
        (MOVEMENT, 'movement'),
        (TIME, 'time'),
        (SPACE, 'space')
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

    exploration = models.CharField(
        max_length=50, default='', choices=EXPLORATION_CHOICES)
    concept = models.CharField(
        max_length=50, default='', choices=CONCEPT_CHOICES)
    element = models.CharField(
        max_length=50, default='', choices=ELEMENT_CHOICES)
    emotion = models.CharField(
        max_length=50, default='', choices=EMOTION_CHOICES)
    temperature = models.FloatField(default=0.8)
    user = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name='music', blank=True, null=True)
    prompt_length = models.CharField(choices=LENGTH_CHOICES)
    input_length = models.CharField(blank=True, max_length=300)
    output = models.TextField(blank=True)

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
        input_temperature = self.temperature
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
            temperature=input_temperature,
        )
        self.output = response['choices'][0]['message']['content']
        self.save()

    def __str__(self):
        return str(self.id)
