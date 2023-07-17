from rest_framework import serializers
from .models import User, Write, VisualArt, Movement


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
