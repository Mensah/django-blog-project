from django.db import models
from django.contrib import admin 

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=60)
    body = models.TextField()
    created = models.DateField()
    updated = models.DateField(auto_now=True)
    def __unicode__(self):
        return self.title

class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created = models.DateField()
    updated = models.DateField(auto_now=True)
    post = models.ForeignKey(Post)

admin.site.register(Post)
admin.site.register(Comment)
