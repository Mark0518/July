from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers

from .models import *

__all__ = [
    'UserProfileModelSerializer',
    'RegisterSerializer',
    'LogInSerializer'
]


# Model Serializer

class UserProfileModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


# View Serializer

class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=32)
    password = serializers.CharField(max_length=32)
    retype_password = serializers.CharField(max_length=32)

    def validate_email(self, value):
        try:
            UserProfile.objects.get(email=value)
            raise serializers.ValidationError('The user already exists!')
        except ObjectDoesNotExist:
            return value


class LogInSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=32)
    password = serializers.CharField(max_length=32)
