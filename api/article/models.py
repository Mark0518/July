from django.db import models

from category.models import Category
from tag.models import Tag


# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=255, unique=True)
    url = models.CharField(max_length=255, unique=True)
    desc = models.TextField()
    body = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    release_time = models.DateTimeField(default='1970-1-1 00:00:00')
    update_time = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    click_count = models.IntegerField(default=0)
    categories = models.ForeignKey(Category)
    tag = models.ManyToManyField(Tag)
