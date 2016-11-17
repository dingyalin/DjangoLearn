# encoding=utf-8
from __future__ import unicode_literals
from django.db import models

# Create your models here.


class BBS(models.Model):
    title = models.CharField(max_length=64)
    summary = models.CharField(max_length=256, blank=True, null=True)
    content = models.TextField()
    author = models.ForeignKey('BBS_user')
    view_count = models.IntegerField()
    ranking = models.IntegerField()
    created_at = models.DateField()
    update_at = models.DateField()
    
    def __str__(self):
        return self.title

class Comments(models.Model):
    title = models.CharField(max_length=32, unique=True)
    

class Category(models.Model):
    pass

class BBS_user(models.Model):
    pass
