from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from player.forms import Addsong, CreateUser
from . models import Song
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def index(request):
    if request.user.is_authenticated:
        songs = Song.objects.filter(access = 'PB')
        privatesongs = Song.objects.filter(access = 'PR',user=request.user);
        protectedsongs = Song.objects.filter(access = 'PT',user = request.user);
        return render(request,'player/index.html',{'songs':songs,'psongs':privatesongs,'protectedsongs':protectedsongs})
    else:
        return redirect('login')
@csrf_exempt  
def login_page(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']
            try:
                email = User.objects.get(email=email.lower()).username
            except:
                messages.error(request,'User Not Found')
                return redirect('login')
            user = authenticate(username=email,password=password)
            if user is not None:
                login(request,user)
                return redirect('index')
            else:
                 messages.error(request,'Invalid login')
                 return redirect('login')
    return render(request,'player/login.html');
@csrf_exempt
def register(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == "POST":
        form = CreateUser(request.POST)
        print("In form")
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=CreateUser()
    return render(request,'player/register.html',{'form':form})

def logout_page(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
@csrf_exempt
def addSong(request):
    if request.method == 'POST':
        form = Addsong(request.POST,request.FILES)
        print("In form")
        if form.is_valid():
            doc=form.save(commit=False)
            if doc.access == 'PR':
                doc.user=request.user
                doc.user.editable=False
                doc.save()
            elif doc.access == 'PB':
                doc.save()
            else:
                doc.save()
            return redirect('index')
    else:
        form = Addsong()
    return render(request,'player/Addsong.html',{'form':form})
    
        


