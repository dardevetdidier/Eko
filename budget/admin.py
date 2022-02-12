from django.contrib import admin
from .models import Operation, Budget, Category


@admin.register(Operation)
class DepositAdmin(admin.ModelAdmin):
    list_display = ['description', 'amount', 'category', 'date_created']


@admin.register(Category)
class DepositAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Budget)
class DepositAdmin(admin.ModelAdmin):
    list_display = ['name', 'balance']

