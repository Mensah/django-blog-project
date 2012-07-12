# Create your views here.
from django.template import Context, loader
from django.shortcuts import render_to_response
from django.http import HttpResponse
from models import Post, Comment 

'''
def post_list(request):
    post_list = Post.objects.all()
    
    print type(post_list)
    print post_list
    
    return HttpResponse(post_list)
'''
def post_list(request):
    posts = Post.objects.all()
    t = loader.get_template('blogg/post_list.html')
    c = Context({'posts':posts})
    return HttpResponse(t.render(c))

def post_detail(request, id, showComments=False):
    posts = Post.objects.get(pk=id)
    comments = posts.comments.all
    '''   html = '<h3>'+str(single_post) + '</h3><br/>' + str(single_post.body)  + '<br/><h5>Comments</h5><br/>'
    comm = ' '
    for i in single_post.comments.all():
        comm += i.body + '<br/>'''
    return render_to_response('blogg/post_detail.html', {'posts':posts, 'comments':comments})

def post_search(request, term):
    posts = Post.objects.filter(body__contains=term) 
    '''res = ' '
    for i in searched:
        res +=  i.title + ' : ' + i.body'''
    return render_to_response('blogg/post_search.html', {'posts':posts, 'term':term})

def home(request):
    return render_to_response('blogg/base.html', {}) 

