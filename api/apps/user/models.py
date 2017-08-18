from django.contrib.auth.models import AbstractUser
from django.db import models

__all__ = ('UserProfile',)


# Create your models here.

class UserProfile(AbstractUser):
    GENDER_CHOICES = (
        ('male', '男'),
        ('female', '女'),
        ('unknown', '未知')
    )
    nick_name = models.CharField(max_length=100, default='')
    gender = models.CharField(choices=GENDER_CHOICES, default='unknown', max_length=20)
    image = models.CharField(max_length=100, default='avatar/avatar.png')
