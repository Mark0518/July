from rest_framework import serializers

from .models import *

__all__ = [
    'CategoryModelSerializer',
    'CategoryListSerializer',
    'CategoryDetailSerializer'
]


# Model Serializer

class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


# View Serializer


class CategoryListSerializer(CategoryModelSerializer):
    article_count = serializers.IntegerField()


class CategoryDetailSerializer(CategoryModelSerializer):
    article_count = serializers.IntegerField()
