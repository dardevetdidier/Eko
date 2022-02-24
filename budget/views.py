from datetime import timedelta

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

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
            return redirect('dashboard')
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('dashboard')
        else:
            return render(request, 'budget/index.html', context={'form': login_form})


@login_required(login_url='index')
def logout_user(request):
    """
    Logout user and return to login page

    """
    logout(request)
    return redirect('index')


@login_required(login_url='index')
def dashboard(request):
    """
    Display dashboard and allows to create a new operation
    """
    today = timezone.now().date()
    date_display = today - timedelta(days=15)
    operations = Operation.objects.filter(date_created__gte=date_display).filter(date_created__lte=today)
    accounts = Account.objects.all()
    if request.method == 'POST':
        create_operation_form = CreateOperationForm(request.POST)
        if create_operation_form.is_valid():
            operation = create_operation_form.save(commit=False)
            account = operation.account
            if operation.operation_type == "Credit":
                account.balance += operation.amount
            else:
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
    """
    Display all accounts. Allows to create a new account
    """
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


@login_required(login_url='index')
def delete_account(request):
    """
    Allows to delete an account
    """
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


@login_required(login_url='index')
def update_operation(request, pk):
    """
    Allows to modify an operation
    """
    operation = get_object_or_404(Operation, pk=pk)
    print(operation.date_created)
    update_operation_form = CreateOperationForm(instance=operation)
    amount = operation.amount
    account = operation.account

    if request.method == 'POST':
        update_operation_form = CreateOperationForm(request.POST, instance=operation)
        if update_operation_form.is_valid():
            print("ok")
            update_operation_form.save()
            if update_operation_form.cleaned_data['amount'] != amount:
                difference = update_operation_form.cleaned_data['amount'] - amount
                if operation.operation_type == "Withdraw":
                    account.balance -= difference
                else:
                    account.balance += difference
                account.save()
        return redirect('dashboard')
    else:

        context = {
            'update_op_form': update_operation_form,
            'operation': operation,
            'account': account
        }
        return render(request, 'budget/update_operation.html', context=context)


@login_required(login_url='index')
def delete_operation(request, pk):
    """
    Allows to delete an operation
    """
    operation = get_object_or_404(Operation, pk=pk)
    print(operation.operation_type)
    if request.method == 'POST':
        account = operation.account
        if operation.operation_type == "Withdraw":
            account.balance += operation.amount
        elif operation.operation_type == "Credit":
            account.balance -= operation.amount
        account.save()
        operation.delete()
        return redirect('dashboard')

    else:
        return render(request, 'budget/delete-operation.html', context={'operation': operation})


@login_required(login_url='index')
def view_categories(request):
    """
    Display all categories of operations. Allows to create a new categoey
    """
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


@login_required(login_url='index')
def delete_category(request, pk):
    """
    Delete a category
    """
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('categories')
    else:
        return render(request, 'budget/delete_category.html', context={'category': category})

