from __future__ import unicode_literals
from django.db import models
  # Create your models here.


class user(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email= models.EmailField()
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class messages(models.Model):
    message = models.TextField(max_length=1000)
      # Notice the association made with ForeignKey for a one-to-many relationship
    user = models.ForeignKey(user)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class comments(models.Model):
    comment = models.TextField(max_length=1000)
           # Notice the association made with ForeignKey for a one-to-many relationship
    user= models.ForeignKey(user)
    message = models.ForeignKey(messages)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
