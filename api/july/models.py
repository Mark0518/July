from django.db import models


# Create your models here.

class Link(models.Model):
    name = models.CharField(max_length=32, unique=True)
    url = models.URLField(unique=True)
    desc = models.TimeField(default='此用户没有添加任何描述')
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)


class July(models.Model):
    title = models.CharField(max_length=80)
    keywords = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    nickname = models.CharField(max_length=100)
    avatar = models.CharField(max_length=128)
    home_desc = models.CharField(max_length=150)
    record_number = models.CharField(max_length=100)
    statistics_code = models.TextField()


class UploadImg(models.Model):
    img = models.ImageField(upload_to='%Y/%m', max_length=128)
