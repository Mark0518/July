from django.db import models

__all__ = ('Categories',)


# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=32, unique=True)
    created_time = models.DateTimeField(auto_now_add=True)
