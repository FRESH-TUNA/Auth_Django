from django import forms
from django.contrib.auth.models import User
from .models import Post

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')

class PostForm(forms.ModelForm):
    title = forms.CharField()
    context = forms.CharField(max_length=20)
    class Meta:
        model = Post
        fields = ('title', 'context')

