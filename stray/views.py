from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'stray/index.html')

def post_list(request):
    return render(request,'stray/post_list.html')

