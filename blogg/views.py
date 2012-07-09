# Create your views here.
from django.template import Context, loader
from django.http import HttpResponse

from models import Post, Comment 


def post_list(request):
    post_list = Post.objects.all()
    
    print type(post_list)
    print post_list
    
    return HttpResponse(post_list)

def post_detail(request, id, showComments=False):
    single_post = Post.objects.get(pk=id)
    return HttpResponse(single_post)

def post_search(request, term):
    pass
  #  searched = Post.objects.value(term)
    #return HttpReponse(searched)

def home(request):
    print 'it works'
    return HttpResponse('hello world. Ete zene?') 

