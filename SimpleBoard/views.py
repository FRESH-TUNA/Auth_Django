from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *
from .forms import *
from django.contrib.auth import login, logout, authenticate
from django.contrib import auth
from django.http import HttpResponse

def index(request):
    posts = Post.objects.all()
    userForm = UserForm()
    loginForm = LoginForm()
    return render(request, 'index.html', {'posts': posts, 'signup_form' : userForm, 'signin_form' : loginForm})

def signup(request):
    if request.method == "GET":
        form = UserForm()
        return render(request, 'signup.html', {'form':form})
    else :
        form = UserForm(request.POST)

        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request, new_user)
            return redirect('index')


def signin(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, 'signin.html', {'form':form})
    else:
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return HttpResponse('로그인 실패. 다시 시도 해보세요.')

def signup(request):
    if request.method == "GET":
        form = UserForm()
        return render(request, 'signup.html', {'form':form})
    else :
        form = UserForm(request.POST)

        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request, new_user)
            return redirect('index')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('index')

def createPost(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            form = PostForm()
            return render(request, 'createPost.html', {'form':form})
        else:
            form = PostForm(request.POST)
            form.save()
            return redirect('index')
    else:
        return redirect('signin')