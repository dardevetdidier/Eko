from django.contrib import admin
from .models import Operation, Account, Category


@admin.register(Operation)
class DepositAdmin(admin.ModelAdmin):
    list_display = ['description', 'amount', 'category', 'account', 'date_created']


@admin.register(Category)
class DepositAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Account)
class DepositAdmin(admin.ModelAdmin):
    list_display = ['name', 'balance']

