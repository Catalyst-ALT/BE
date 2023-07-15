from rest_framework import serializers
from .models import User, Poem


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class PoemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poem
        fields = '__all__'

