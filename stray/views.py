from django.shortcuts import redirect, render
from .models import Post

# Create your views here.

def index(request):
    return render(request,'stray/index.html')


def post_list(request):
    postlist = Post.objects.all()
    return render(request,'stray/post_list.html',{'postlist':postlist})

def posting(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'stray/posting.html',{'post':post})

def new_post(request):
    if request.method == 'POST':
        if request.POST['mainphoto']:
            new_cat = Post.objects.create(
                postname=request.POST['postname'],
                contents=request.POST['contents'],
                mainphoto=request.POST['mainphoto'],
            )
        else :
            new_cat = Post.objects.create(
                postname=request.POST['postname'],
                contents=request.POST['contents'],
                mainphoto=request.POST['mainphoto'],
            )
        return redirect('/post_list/')
    return render(request, 'stray/new_post.html')

def remove_post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method =='POST':
        post.delete()
        return redirect('/post_list/')
    return render(request, 'stray/remove_post.html',{'Post':post})