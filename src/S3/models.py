# encoding=utf-8
from __future__ import unicode_literals

from django.db import models

class Path(models.Model):
    name = models.CharField(max_length=1000)
    up_path_id = models.IntegerField()
    
    def __str__(self):              # __unicode__ on Python 2
        return self.name
    
class File(models.Model):
    name = models.CharField(max_length=50)
    path = models.ForeignKey(Path, on_delete=models.CASCADE)
    
    def __str__(self):              # __unicode__ on Python 2
        return self.name
