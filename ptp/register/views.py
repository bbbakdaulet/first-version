from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import RegisterForm
import os

def register(request):
    if request.method =="POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request,'base.html', {"form":form})
    else:
        form=RegisterForm()
        
    return render(request,'register.html', {"form":form})
