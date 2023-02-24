from rest_framework import serializers
from .models import Work, Artist, Client

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ['name', 'username', 'email']

class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = ('id', 'link', 'work_type')

class ArtistSerializer(serializers.ModelSerializer):
    works = WorkSerializer(many=True, read_only=True)
    class Meta:
        model = Artist
        fields = ('id', 'name', 'works')
