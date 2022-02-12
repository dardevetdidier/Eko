from django.contrib import admin
from .models import Deposit, Withdraw, Account, Category


@admin.register(Deposit)
class DepositAdmin(admin.ModelAdmin):
    list_display = ['description', 'amount', 'date_created']


@admin.register(Withdraw)
class DepositAdmin(admin.ModelAdmin):
    list_display = ['description', 'amount', 'category', 'date_created']


@admin.register(Category)
class DepositAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Account)
class DepositAdmin(admin.ModelAdmin):
    list_display = ['name', 'balance', 'owner']

