from django.db import models
from django.contrib import admin 

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=60)
    body = models.TextField()
    created = models.DateField(auto_now=True)
    updated = models.DateField(auto_now=True)
    def __unicode__(self):
        return self.title
    def first_sixty(self):
        return self.body[:60]
    def get_absolute_url(self):
        return "/blogg/posts/%i/true" % self.id


class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created = models.DateField(auto_now=True)
    updated = models.DateField(auto_now=True)
    post = models.ForeignKey(Post, related_name = 'comments')
    def __unicode__(self):
        return self.author
    def first_sixty(self):
        return self.body[:60]
        
class CommentInline(admin.TabularInline):
    model = Comment 

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'updated')
    search_fields = ('title', 'body')
    list_filter = ('created', 'updated')
    inlines = [CommentInline]   

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'first_sixty','created', 'updated' )
    list_filter = ('created', 'author')
    inlines = [CommentInline]    

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)

