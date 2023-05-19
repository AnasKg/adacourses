from typing import Any, Dict
from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.http import Http404
from .models import Post, Comment, Product
from django.contrib.auth.models import User
from .forms import MyForm, PostForm, ProductForm, CommentForm
from django.views import View, generic
from django.urls import reverse_lazy

# Create your views here.

def index(request):
    return HttpResponse('<h1>Hello World!</h1>')


def post_list(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'posts/post_list.html', context=context)

class PostListView(generic.ListView):
    # model = Post
    queryset = Post.objects.all().order_by('-created_at')
    context_object_name = 'posts'
    template_name = 'posts/post_list.html'


class PostDetailView(generic.DetailView):
    queryset = Post.objects.all()
    context_object_name = 'post'
    template_name = 'posts/post_detail.html'
    pk_url_kwarg = 'post_id'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        context['comments'] = Comment.objects.filter(post=post)
        context['form'] = CommentForm()
        return context

class PostCreateView(generic.CreateView):
    model = Post
    fields = ('title', 'content', 'author')
    template_name = 'posts/create_post.html'
    # success_url = '/posts/'

    def get_success_url(self):
        post = self.object
        return reverse_lazy('post_detail', kwargs={'post_id': post.id})

class PostUpdateView(generic.UpdateView):
    model = Post
    fields = ('title', 'content', 'author')
    template_name = 'posts/edit_post.html'
    # success_url = '/posts/'
    pk_url_kwarg = 'post_id'

    def get_success_url(self):
        post = self.object
        return reverse_lazy('post_detail', kwargs={'post_id': post.id})

class CommentCreateView(generic.CreateView):
    model = Comment
    fields = ['author', 'content']
    template_name = 'posts/comment_form.html'

    def form_valid(self, form):
        post = get_object_or_404(Post, id=self.kwargs['post_id'])
        form.instance.post = post
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'post_id': self.kwargs['post_id']})


class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = 'posts/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')
    pk_url_kwarg = 'post_id'


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = Comment.objects.filter(post=post)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            # content = form.cleaned_data['content']
            # author = form.cleaned_data['author']
            # Comment.objects.create(
            #     post=post,
            #     content=content,
            #     author=author
            # )
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_detail', post_id=post_id)
    else:
        form = CommentForm()
    
     
    context = {'post': post, 'comments': comments, 'form':form}

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
            # title = form.cleaned_data['title']
            # content = form.cleaned_data['content']
            # author = form.cleaned_data['author']
            # post = Post.objects.create(title=title, content= content , author = author)

            post = form.save()

            return redirect('post_detail', post_id = post.id)

    else:
        form = PostForm()

    return render(request, 'posts/create_post.html',{'form':form})


def see_product(request):
    if request.method == 'GET':
        prod_data = Product.objects.all()
        return render(request, 'posts/product_list.html', {'products':prod_data})

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            price = form.cleaned_data['price']
            product = Product.objects.create(name=name, price=price)
            return redirect('product_list') 
    else:
        form = ProductForm()
    
    return render(request, 'posts/create_product.html', {'form':form})


def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        # form = PostForm(request.POST)
        # if form.is_valid():
        #     post.title = form.cleaned_data['title']
        #     post.content = form.cleaned_data['content']
        #     post.save()

        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()

            return redirect('post_detail', post_id=post.id)
    else:
        # form = PostForm(initial={
        #     'title': post.title,
        #     'content': post.content,
        #     'author': post.author
        # })
        form = PostForm(instance=post)
    
    return render(request, 'posts/post_edit.html', {'form': form, 'post': post})


def edit_comment(request, post_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment.content = form.cleaned_data['content']
            comment.author = form.cleaned_data['author']
            comment.save()

            return redirect('post_detail', post_id=post_id)
    
    else:
        form = CommentForm(initial={
            'author': comment.author,
            'content': comment.content
        })
    
    context = {'form': form, 'comment': comment}

    return render(request, 'posts/edit_comment.html', context)