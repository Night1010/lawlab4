from dataclasses import field
from rest_framework import serializers
from .models import Adventurer,Image


class AdventureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adventurer
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'
