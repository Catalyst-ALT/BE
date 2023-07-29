from rest_framework import serializers
from .models import (
    User,
    Write,
    VisualArt,
    Movement,
    Music,
    Welcome,
    Definition,

)


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username'
        ]


class WriteInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Write
        fields = [
            'id',
            'user',
            'theme',
            'category',
            'sentiment',
            'emotion',
            'prompt_length',
            'input_length',
            'save_prompt',
        ]


class WriteOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Write
        fields = [
            'id',
            'user',
            'theme',
            'category',
            'sentiment',
            'emotion',
            'prompt_length',
            'input_length',
            'created_at',
            'output',
            'note',
            'save_prompt',
        ]


class VisualArtInputSerializer(serializers.ModelSerializer):

    class Meta:
        model = VisualArt
        fields = [
            'id',
            'user',
            'medium',
            'theme',
            'sentiment',
            'emotion',
            'prompt_length',
            'input_length',
            'save_prompt',
        ]


class VisualArtOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisualArt
        fields = [
            'id',
            'user',
            'medium',
            'theme',
            'sentiment',
            'emotion',
            'prompt_length',
            'input_length',
            'created_at',
            'output',
            'note',
            'save_prompt',
        ]


class MovementInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movement
        fields = [
            'id',
            'user',
            'theme',
            'somatic',
            'sentiment',
            'emotion',
            'prompt_length',
            'input_length',
            'save_prompt',
        ]


class MovementOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movement
        fields = [
            'id',
            'user',
            'theme',
            'somatic',
            'sentiment',
            'emotion',
            'prompt_length',
            'input_length',
            'created_at',
            'output',
            'note',
            'save_prompt',
        ]


class MusicInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = [
            'id',
            'user',
            'exploration',
            'concept',
            'element',
            'emotion',
            'prompt_length',
            'input_length',
            'save_prompt',
        ]


class MusicOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = [
            'id',
            'user',
            'exploration',
            'concept',
            'element',
            'emotion',
            'prompt_length',
            'input_length',
            'created_at',
            'output',
            'note',
            'save_prompt',
        ]


class AllMediumsSerializer(serializers.ModelSerializer):
    music = MusicOutputSerializer(many=True, read_only=True)
    visual_arts = VisualArtOutputSerializer(many=True, read_only=True)
    movements = MovementOutputSerializer(many=True, read_only=True)
    writes = WriteOutputSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'music',
            'visual_arts',
            'movements',
            'writes'
        ]


class WelcomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Welcome
        fields = [
            'id',
            'output_text',
        ]


class DefinitionInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Definition
        fields = [
            'id',
            'word',
        ]


class DefinitionOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Definition
        fields = [
            'id',
            'word',
            'definition',
            'synonym',
            'antonym',
            'sentence',
            'joke',
            'color',
        ]
