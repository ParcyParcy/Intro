from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.shortcuts import render, get_object_or_404


def index(request):
    posts = Post.objects.order_by('-published')
    return render(request, 'posts/index.html')

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'posts/post_detail.html', {'post': post})

def profile(request):
    return render(request, 'posts/profile.html')

def post_list(request):
    posts = Post.objects.order_by('-published')
    return render(request, 'posts/post_list.html', {'posts': posts})

def contact(request):
    return render(request, 'posts/contact.html')

