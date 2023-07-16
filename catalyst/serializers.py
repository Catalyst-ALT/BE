from rest_framework import serializers
from .models import User, Poem, Prompt


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class PoemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poem
        fields = '__all__'


class PoemOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poem
        fields = ['output']
