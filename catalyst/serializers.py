from rest_framework import serializers
from .models import User, Write, VisualArt, Movement, Music, Note, Welcome


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class WriteInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Write
        fields = '__all__'


class WriteOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Write
        fields = '__all__'


class VisualArtInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisualArt
        fields = '__all__'


class VisualArtOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisualArt
        fields = '__all__'


class MovementInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movement
        fields = '__all__'


class MovementOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movement
        fields = '__all__'


class MusicInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = '__all__'


class MusicOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = '__all__'


class AllPromptsArchiveSerializer(serializers.ModelSerializer):
    music = MusicOutputSerializer(many=True, read_only=True)
    visual_arts = VisualArtOutputSerializer(many=True, read_only=True)
    movements = MovementOutputSerializer(many=True, read_only=True)
    writes = WriteOutputSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['username', 'music', 'visual_arts', 'movements', 'writes']


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'


class WelcomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Welcome
        fields = '__all__'
