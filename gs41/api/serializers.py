from rest_framework import serializers
from .models import Singer, Song

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'duration', 'singer']  # Ensure this is correctly aligned

class SingerSerializer(serializers.ModelSerializer):
    sung_by = SongSerializer(many=True, read_only=True, source='songs')  # source='songs' matches the related_name in the Song model

    class Meta:
        model = Singer
        fields = ['id', 'name', 'gender', 'sung_by']
