from django import forms
from django.contrib.auth.models import User
from .models import Post, Comment


class MyForm(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField()
    text = forms.CharField(max_length=255)


# class PostForm(forms.Form):
#     title = forms.CharField(max_length=255)
#     content = forms.CharField()
#     author = forms.ModelChoiceField(queryset=User.objects.all())

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'content', 'author')
    

class ProductForm(forms.Form):
    name = forms.CharField(max_length=255)
    price = forms.IntegerField()


# class CommentForm(forms.Form):
#     content = forms.CharField(max_length=255)
#     author = forms.ModelChoiceField(queryset=User.objects.all())


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('content', 'author')
