from django.shortcuts import render,redirect
from django .contrib.auth import login,logout,authenticate
from .form import *
from .models import *


# Create your views here.
def register(request):
    form=UserForm
    if request.method=="POST":
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("anasayfa")
    context={
        "form":form
    }
    return render(request,"register.html",context)

def userLogin(request):
    if request.method=="POST":
        username=request.POST["username"]
        userpass=request.POST["password"]

        user=authenticate(request,username=username,password=userpass)
        if user is not None:
            login(request,user)
            return redirect('profiles')
        else:
            return render(request,"login.html")
    return render(request,"login.html")

def profiles(request):
    kullanicilar=Profiles.objects.filter(owner=request.user)
    context={
        "kullanicilar":kullanicilar
    }
    return render(request,"browse.html",context)

def createProfil(request):
    form=ProfilForm()
    if request.method=="POST":
        form=ProfilForm(request.POST,request.FILES)
        if form.is_valid():
            profile=form.save(commit=False)
            profile.owner=request.user
            profile.save()
            return redirect("profiles")
        
    context={
        "form":form
    }
    return render(request,"create-profile.html",context)

def oturumKapat(request):
    logout(request)
    return redirect('anasayfa')
def userProfil(request):
    profil=request.user
    context={
        "profil":profil
    }
    return render(request,"hesap.html",context)

def deleteUser(request):
    profil=request.user
    profil.delete()
    return redirect("anasayfa")