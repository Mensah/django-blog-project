from django.db import models
from django.contrib import admin 

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=60)
    P_body = models.TextField()
    P_created = models.DateField()
    P_updated = models.DateField(auto_now=True)
    def __unicode__(self):
        return self.title

class Comment(models.Model):
    author = models.CharField(max_length=60)
    C_body = models.TextField()
    C_created = models.DateField()
    C_updated = models.DateField(auto_now=True)
    post = models.ForeignKey(Post)
    def first_sixty(self):
        return self.body[:60]
        
class CommentInline(admin.TabularInline):
    model = Comment 

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'P_created', 'P_updated')
    search_fields = ('title', 'P_body')
    list_filter = ('P_created', 'P_updated')
    inlines = [CommentInline]   

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'first_sixty','C_created', 'C_updated' )
    list_filter = ('C_created', 'author')
    inlines = [CommentInline]    

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)

