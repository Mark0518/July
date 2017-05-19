from rest_framework import serializers

from .models import *

__all__ = [
    'TagModelSerializer',
    'TagListSerializer',
    'TagDetailSerializer'
]


# Model Serializer

class TagModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


# View Serializer


class TagListSerializer(TagModelSerializer):
    article_count = serializers.IntegerField()


class TagDetailSerializer(TagModelSerializer):
    article_count = serializers.IntegerField()
