#coding=utf8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Todo(models.Model):
    content = models.TextField(u'Content')
    state = models.BooleanField(default='False')
    


    

