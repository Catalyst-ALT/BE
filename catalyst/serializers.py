from rest_framework import serializers
from .models import User, Poem, Prompt, VisualArt


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class PoemInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poem
        fields = '__all__'


class PoemOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poem
        fields = '__all__'


class VisualArtInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisualArt
        fields = '__all__'


class VisualArtOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisualArt
        fields = '__all__'
