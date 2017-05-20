from django.contrib.auth.models import AbstractUser
from django.db import models

__all__ = [
    'UserProfile',
    'EmailCaptchaCode'
]


# Create your models here.

class UserProfile(AbstractUser):
    avatar = models.ImageField(upload_to='avatar/%Y/%m', max_length=128, default='avatar/avatar.png')


class EmailCaptchaCode(models.Model):
    code = models.IntegerField()
    email = models.EmailField(max_length=128)
    send_time = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
