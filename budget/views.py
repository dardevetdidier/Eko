from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import LoginForm


def index(request):
    """
    Display a login form and checks if user exists then log in.
    """
    login_form = LoginForm()
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, "Erreur dans le nom d'utilisateur et/ou le mot de passe")
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('dashboard')
        else:
            return render(request, 'budget/index.html', context={'form': login_form})


@login_required
def logout_user(request):
    """
    Logout user and return to login page

    """
    logout(request)
    return redirect('index')


@login_required(login_url='index')
def budget(request):
    return render(request, 'budget/dashboard.html')


