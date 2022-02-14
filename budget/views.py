from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import LoginForm, CreateAccountForm, DeleteForm, CreateOperationForm, CreateCategoryForm
from .models import Account, Operation, Category


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


def logout_user(request):
    """
    Logout user and return to login page

    """
    logout(request)
    return redirect('index')


@login_required(login_url='index')
def dashboard(request):
    operations = Operation.objects.all()[:6]
    accounts = Account.objects.all()
    if request.method == 'POST':
        create_operation_form = CreateOperationForm(request.POST)
        if create_operation_form.is_valid():
            operation = create_operation_form.save(commit=False)
            account = operation.account
            account.balance -= operation.amount
            account.save()
            operation.save()

        return redirect('dashboard')
    else:
        create_operation_form = CreateOperationForm()
        context = {'accounts': accounts,
                   'operations': operations,
                   'create_operation_form': create_operation_form}
        return render(request, 'budget/dashboard.html', context=context)


@login_required(login_url='index')
def view_accounts(request):
    if request.method == 'POST':
        create_account_form = CreateAccountForm(request.POST)

        if create_account_form.is_valid():
            create_account_form.save()
        return redirect('dashboard')

    else:
        accounts = Account.objects.all()

        create_account_form = CreateAccountForm()
        context = {'accounts': accounts,
                   'create_account_form': create_account_form}

    return render(request, 'budget/accounts.html', context=context)


def delete_account(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        account = Account.objects.filter(name__exact=name)
        account.delete()
        return redirect("accounts")
    else:
        delete_form = DeleteForm()
        accounts = Account.objects.all()
    context = {'delete_form': delete_form,
               'accounts': accounts}
    return render(request, 'budget/delete_account.html', context=context)


def detail_operation(request, pk):
    operation = get_object_or_404(Operation, pk=pk)
    context = {'operation': operation}
    return render(request, 'budget/operation-detail.html', context=context)


def delete_operation(request, pk):
    operation = get_object_or_404(Operation, pk=pk)
    if request.method == 'POST':
        account = operation.account
        account.balance += operation.amount
        account.save()
        operation.delete()
        return redirect('dashboard')

    else:
        return render(request, 'budget/delete-operation.html', context={'operation': operation})


def view_categories(request):
    if request.method == 'POST':
        create_category_form = CreateCategoryForm(request.POST)
        if create_category_form.is_valid():
            create_category_form.save()
        return redirect('categories')

    else:
        create_category_form = CreateCategoryForm()
        categories = Category.objects.all()
        context = {'categories': categories,
                   'create_category_form': create_category_form}

    return render(request, 'budget/categories.html', context=context)


def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('categories')
    else:
        return render(request, 'budget/delete_category.html', context={'category': category})

