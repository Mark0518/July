from rest_framework import serializers

from .models import *

__all__ = [
    'ArticleModelSerializer',
    'ArticleListSerializer',
    'ArticleDetailSerializer'
]


# Model Serializer

class ArticleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


# View Serializer


class ArticleListSerializer(ArticleModelSerializer):
    article_count = serializers.IntegerField()


class ArticleDetailSerializer(ArticleModelSerializer):
    article_count = serializers.IntegerField()
