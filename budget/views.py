from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render

from .forms import LoginForm


def index(request):
    """
    Display a login form and checks if user exists then log in.
    """
    login_form = LoginForm()
    if request.method == 'Post':
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
        else:
            messages.info(request, "Erreur dans le nom d'utilisateur ou le mot de passe")
    return render(request, 'budget/index.html', context={'form': login_form})
