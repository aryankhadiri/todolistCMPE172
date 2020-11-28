# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from .models import User

# Create your views here.
def login_view(request):
    error = ''
    form = LoginForm()

    if request.user.is_authenticated:
        return redirect('/userhome')
    if request.method == "POST":
        if form.is_valid:
            user_email = request.POST.get('email')
            user_password = request.POST.get('password')
            user = authenticate(request, email = user_email, password = user_password)
            if user is not None:
                login(request, user)
                return redirect("login")
            else:
                error = 'Incorrect email/password combination.'

    context = {
        'form':form,
        'error':error,
    }
    return render(request, 'login.html', context)

def logout_view(request):
    logout(request)
    return redirect ('login')

def register(request):
    form = LoginForm()
    error = ''

    if request.method == "POST":
        form2 = LoginForm(request.POST)
        if form2.is_valid():
            user = form2.save(commit = "False")
    context = {
        'form':form
    }
    return render (request, 'register.html', context)
