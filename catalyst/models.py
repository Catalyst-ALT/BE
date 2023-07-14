from django.db import models
from django.contrib.auth.models import AbstractUser


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
    ADVOCACY = 'advocacy'
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
        (ADVOCACY, 'advocacy'),
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
    TRANSIENCE = 'transcience'
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
        max_length=50, default='', null=True, blank=True)
    input_emotion = models.CharField(
        max_length=50, default='', null=True, blank=True)
    user = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name='poems', blank=True, null=True)

    def __str__(self):
        return self.user
