from django.shortcuts import redirect, render

from main.models import Post
from .forms import  PostForm, RegisterForm, TimeIn
from  django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import  login_required
from .models import Post,TimeIn_Out

import datetime
# Create your views here.

@login_required(login_url="/login")
def home(request):

    posts = Post.objects.all()
   
    
    if request.method =="POST":
        if request.POST.get("timeinn"):
            savetimein = TimeIn_Out()
            savetimein.ParkerName = request.user
            savetimein.Parker = request.user
            savetimein.save()
        elif request.POST.get("timeout"):
            return redirect('/info')


        elif request.POST.get("post-id"):
            post_id = request.POST.get("post-id")
            post = Post.objects.filter(id=post_id).first()
            post.delete()
            
           
        

    return render(request, 'main/home.html', {"posts": posts })
    

@login_required(login_url="/login")
def add_car (request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.Owner = request.user 
            post.save()
            return redirect('/home')

    else:
        form = PostForm()
    
    return render(request, 'main/add-car.html', {"form": form})

def info(request):
    return render(request,'main/info.html')

def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = RegisterForm()

    return render(request,'registration/sign_up.html', {"form":form})



@login_required(login_url="/login")
def timeLog(request):
    return



@login_required(login_url="/login")
def timein(request):
    if request.method == 'POST':
        form = TimeIn(request.POST)
        if form.is_valid():
           form.save()
           
    return render(request,'registration/sign_up.html', {"form":form})
        

@login_required(login_url="/login")
def Timeout(request):
    return

