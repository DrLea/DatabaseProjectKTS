from rest_framework import serializers
from .models import *

from django.utils.timezone import now
from django.contrib.auth.hashers import make_password

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)

        # here, token is an instance of Token (from rest_framework_simplejwt.tokens)
        token = self.get_token(self.user)


        data['user_id'] = token['user_id']

        return data




class InterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interest
        fields = "__all__"
        


class UserSerializer(serializers.ModelSerializer):
    interests = InterestSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = User
        fields = ['nickname', 'email', 'password', 'image', 'age', 'interests', 'description']

    def create(self, validated_data):
        password = validated_data.pop('password')
        password = make_password(password)
        instance = self.Meta.model.objects.create(password=password, **validated_data)
        return instance


class ContentSerializer(serializers.ModelSerializer):
    isApproved = serializers.ReadOnlyField(default=False)
    date = serializers.ReadOnlyField(default=now())

    class Meta:
        model = Content
        fields = ['id', 'name', 'description', 'image', 'isApproved', 'tag', 'date']


class _ContentSerializer(serializers.ModelSerializer):
    content = ContentSerializer(source='content_id', read_only=False)

    class Meta:
        model = Content
        fields = ['content', 'user']

    def create(self, validated_data):
        content_data = validated_data.pop('content_id')
        content = Content.objects.create(**content_data)
        user = validated_data["user"]
        content.isApproved = user.is_staff
        content.save()
        instance = self.Meta.model.objects.create(content_id=content, **validated_data)
        return instance

    def update(self, instance, validated_data):
        content_data = validated_data.pop('content_id')
        content = instance.content_id
        for attr, value in content_data.items():
            setattr(content, attr, value)
        content.save()
        instance = super().update(instance, validated_data)
        return instance


class EventSerializer(_ContentSerializer):
    location = serializers.URLField()
    user = serializers.ReadOnlyField(source='user.id')

    class Meta(_ContentSerializer.Meta):
        model = Event
        fields = _ContentSerializer.Meta.fields + ['location', 'id']


class BookSerializer(_ContentSerializer):
    source = serializers.FileField()
    user = serializers.ReadOnlyField(source='user.id')

    class Meta(_ContentSerializer.Meta):
        model = Book
        fields = _ContentSerializer.Meta.fields + ['source', 'id']



class VideoSerializer(_ContentSerializer):
    source = serializers.FileField()
    user = serializers.ReadOnlyField(source='user.id')

    class Meta(_ContentSerializer.Meta):
        model = Video
        fields = _ContentSerializer.Meta.fields + ['source', 'id']


class FileSerializer(_ContentSerializer):
    file = serializers.FileField()
    user = serializers.ReadOnlyField(source='user.id')

    class Meta(_ContentSerializer.Meta):
        model = File
        fields = _ContentSerializer.Meta.fields + ['file', 'id']


class PodcastSerializer(_ContentSerializer):
    file = serializers.FileField()
    user = serializers.ReadOnlyField(source='user.id')

    class Meta(_ContentSerializer.Meta):
        model = Podcast
        fields = _ContentSerializer.Meta.fields + ['file', 'id']


class CommentSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source='user_id.id')

    class Meta:
        model = Comment
        fields = ['id', 'user_id', 'content_id', 'text']