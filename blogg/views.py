# Create your views here.
from django.template import Context, loader
from django.shortcuts import render_to_response
from django.http import HttpResponse
from models import Post, Comment
from django.forms import ModelForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect

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

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        exclude=['post']
        
@csrf_exempt
def post_detail(request, id, showComments=False):
    posts = Post.objects.get(pk=id)
    if request.method =="POST":
        comment = Comment(post=posts)
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(request.path)
    else:
        form =CommentForm()    
    comments = posts.comments.all()
    return render_to_response('blogg/post_detail.html', {'posts':posts, 'comments':comments, 'form':form})

@csrf_exempt
def edit_comment(request,id):
    comment = Comment.objects.get(pk=id)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(comment.post.get_absolute_url())
    else:
        form =CommentForm(instance = comment)
    
    
    return render_to_response('blogg/edit_template.html', {'comment':comment ,'form':form})

def post_search(request, term):
    posts = Post.objects.filter(body__contains=term) 
    '''res = ' '
    for i in searched:
        res +=  i.title + ' : ' + i.body'''
    return render_to_response('blogg/post_search.html', {'posts':posts, 'term':term})

def home(request):
    return render_to_response('blogg/base.html', {}) 

