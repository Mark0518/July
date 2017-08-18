from django.db import models

from category.models import Categories
from tag.models import Tag

__all__ = ('Article',)


# Create your models here.

class Article(models.Model):
    STATUS_CHOICES = (
        ('0', '发布'),
        ('1', '存稿'),
    )

    title = models.CharField(max_length=255, unique=True)
    url = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    body = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    release_time = models.DateTimeField(default='1970-1-1 00:00:00')
    status = models.CharField(default=0, max_length=1, choices=STATUS_CHOICES)
    read = models.IntegerField(default=0)
    categories = models.ForeignKey(Categories)
    tag = models.ManyToManyField(Tag)
