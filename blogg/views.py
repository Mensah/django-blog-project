# Create your views here.
from django.template import Context, loader
from django.http import HttpResponse
import re
from models import Post, Comment 


def post_list(request):
    post_list = Post.objects.all()
    
    print type(post_list)
    print post_list
    
    return HttpResponse(post_list)

def post_detail(request, id, showComments=False):
    single_post = Post.objects.get(pk=id)
    html = '<h3>'+str(single_post) + '</h3><br/>' + str(single_post.body)  + '<br/><h5>Comments</h5><br/>'
    comm = ' '
    for i in single_post.comments.all():
        comm += i.body + '<br/>'
    return HttpResponse(single_post)

def post_search(request, term):
    searched = Post.objects.filter(body__contains=term)
    res = ' '
    for i in searched:
        res +=  i.title + ' : ' + i.body
        
    return HttpResponse(res)

def home(request):
    print 'it works'
    return HttpResponse('hellurrrr world. Ete zene?') 

