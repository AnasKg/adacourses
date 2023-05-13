from django.shortcuts import render, HttpResponse, get_object_or_404
from django.http import Http404
from .models import Post, Comment
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    return HttpResponse('<h1>Hello World!</h1>')


def post_list(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'posts/post_list.html', context=context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = Comment.objects.filter(post=post)
    context = {'post': post, 'comments': comments}

    return render(request, 'posts/post_detail.html', context=context)


def users_list(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'posts/user_list.html', context=context)


def user_detail(request, user_id):
    user = get_object_or_404(User, id=user_id)
    context = {'user': user}
    return render(request, 'posts/user_detail.html', context=context)