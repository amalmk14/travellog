from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .form import *


# Create your views here.

def home(request):
    return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('travel:allPlace')
        else:
            messages.info(request,'Invalid Details')
            return redirect('login:login')
    return render(request,'login.html')

def SignUp(request):
    if request.method == 'POST':
        username=request.POST['username']
        first_name=request.POST['first_name']
        # last_name=request.POST['last_name']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Already Taken')
                return redirect('login:signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Already Taken')
                return redirect('login:signup')
            else:
                user=User.objects.create_user(username=username,password=password1,first_name=first_name,email=email)
                user.save();

        else:
            messages.info(request,'Password not matched')
            return redirect('login:signup')
        return redirect('login:login')
    return render(request,'signup.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

@login_required(login_url='/login/')
def updateUser(request,pk):
    user = User.objects.get(pk=pk)
    form = Editprofile(request.POST, instance=user)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('travel:allPlace')
        else:
            form = Editprofile(instance=user)
    return render(request,'editprofile.html',{'form':form , 'user':user})

@login_required(login_url='/login/')
def userProfile(request,pk):
    user = User.objects.get(pk=pk)
    return render(request,'navbar.html',{'user':user})