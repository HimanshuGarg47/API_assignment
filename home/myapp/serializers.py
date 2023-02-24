from rest_framework import serializers
from .models import Work, Artist, Client

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Client
        fields = ('username', 'password')

    def create(self, validated_data):
        user = Client.objects.create(name=validated['name'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = ('id', 'link', 'work_type')

class ArtistSerializer(serializers.ModelSerializer):
    works = WorkSerializer(many=True, read_only=True)
    class Meta:
        model = Artist
        fields = ('id', 'name', 'works')
