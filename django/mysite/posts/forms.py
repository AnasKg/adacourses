from django import forms
from django.contrib.auth.models import User


class MyForm(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField()
    text = forms.CharField(max_length=255)


class PostForm(forms.Form):
    title = forms.CharField(max_length=255)
    content = forms.CharField()
    author = forms.ModelChoiceField(queryset=User.objects.all())