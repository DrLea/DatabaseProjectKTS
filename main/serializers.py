from rest_framework import serializers
from .models import *

from django.utils.timezone import now


class InterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interest
        fields = "__all__"
        


class UserSerializer(serializers.ModelSerializer):
    interests = InterestSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = User
        fields = ['nickname', 'email', 'image', 'age', 'interests', 'description']


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