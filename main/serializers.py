from rest_framework import serializers
from .models import *


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
    user_id = serializers.ReadOnlyField(default=serializers.CurrentUserDefault())
    isApproved = serializers.ReadOnlyField(source="user_id.is_staff")
    date = serializers.ReadOnlyField()

    class Meta:
        model = Content
        fields = ['id', 'user_id', 'name', 'description', 'image', 'isApproved', 'tag', 'date']


class _ContentSerializer(ContentSerializer):
    date = serializers.DateTimeField(default=serializers.DateTimeField())

    def create(self, validated_data):
        content_data = {}
        for field in super().fields:
            content_data[field] = validated_data.pop(field)
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

    class Meta(_ContentSerializer.Meta):
        model = Event
        fields = _ContentSerializer.Meta.fields + ['location']


class BookSerializer(_ContentSerializer):
    source = serializers.FileField()
    user_id = serializers.ReadOnlyField(source='user_id.id')

    class Meta(_ContentSerializer.Meta):
        model = Book
        fields = _ContentSerializer.Meta.fields + ['source']


class VideoSerializer(_ContentSerializer):
    source = serializers.FileField()

    class Meta(_ContentSerializer.Meta):
        model = Video
        fields = _ContentSerializer.Meta.fields + ['source']


class FileSerializer(_ContentSerializer):
    file = serializers.FileField()

    class Meta(_ContentSerializer.Meta):
        model = File
        fields = _ContentSerializer.Meta.fields + ['file']


class PodcastSerializer(_ContentSerializer):
    file = serializers.FileField()

    class Meta(_ContentSerializer.Meta):
        model = Podcast
        fields = _ContentSerializer.Meta.fields + ['file']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user_id', 'content_id', 'text']