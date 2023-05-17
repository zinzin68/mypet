from django.shortcuts import render
from .models import Post

# Create your views here.

def index(request):
    return render(request,'stray/index.html')

def post_list(request):
    postlist = Post.objects.all()
    return render(request,'stray/post_list.html',{'postlist':postlist})

