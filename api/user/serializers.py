from datetime import timedelta

from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from rest_framework import serializers

from api.static import CODE_LIFETIME
from .models import *

__all__ = [
    'UserProfileModelSerializer',
    'RegisterSerializer',
    'LogInSerializer',
    'RestPasswordSerializer'
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
    code = serializers.IntegerField()

    def validate_email(self, value):
        try:
            UserProfile.objects.get(email=value)
            raise serializers.ValidationError('The user already exists!')
        except ObjectDoesNotExist:
            return value

    def validate_code(self, value):
        try:
            EmailCaptchaCode.objects.get(code=value, status=True, send_time__lt=timezone.now() + timedelta(minutes=CODE_LIFETIME))
            return value
        except ObjectDoesNotExist:
            raise serializers.ValidationError('Verification code does not exist!')

    def validate(self, data):
        password = data['password']
        retype_password = data['retype_password']
        if password != retype_password:
            raise serializers.ValidationError(code=400, detail='Two passwords are inconsistent!')
        return data


class LogInSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=32)
    password = serializers.CharField(max_length=32)

    def validate_email(self, value):
        try:
            UserProfile.objects.get(email=value)
            return value
        except ObjectDoesNotExist:
            raise serializers.ValidationError('User does not exist!')


class RestPasswordSerializer(serializers.Serializer):
    password = serializers.CharField()
    retype_password = serializers.CharField()
    code = serializers.IntegerField()

    def validate_code(self, value):
        try:
            EmailCaptchaCode.objects.get(code=value, status=True, send_time__lt=timezone.now() + timedelta(minutes=CODE_LIFETIME))
            return value
        except ObjectDoesNotExist:
            raise serializers.ValidationError('Verification code does not exist!')

    def validate(self, data):
        password = data['password']
        retype_password = data['retype_password']
        if password != retype_password:
            raise serializers.ValidationError(code=400, detail='Two passwords are inconsistent!')
        return data
