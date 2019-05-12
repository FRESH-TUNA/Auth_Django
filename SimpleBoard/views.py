from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import *
from django.contrib.auth import login, authenticate
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

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
            return redirect('signin')
        else:
            return HttpResponse('로그인 실패. 다시 시도 해보세요.')
