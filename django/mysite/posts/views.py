from django.shortcuts import render, HttpResponse, get_object_or_404
from django.http import Http404
from .models import Post, Comment
from django.contrib.auth.models import User
from .forms import MyForm, PostForm

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

def test_form(request):
    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            text = form.cleaned_data['text']
            print(name)
            print(age)
            print(text)
            return redirect('post_list')
    else:
        form = MyForm()

    return render(request, 'posts/test_form.html', {'form':form})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            author = form.cleaned_data['author']
            post = Post.objects.create(title=title, content= content , author = author)

            return redirect('post_detail', post_id = post.id)

    else:
        form = PostForm()

    return render(request, 'posts/create_post.html',{'form':form})