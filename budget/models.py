from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Account(models.Model):
    name = models.CharField(max_length=150)
    balance = models.FloatField()

    def __str__(self):
        return self.name


class Operation(models.Model):
    description = models.CharField(max_length=150)
    amount = models.FloatField()
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, related_name='operations_category')
    account = models.ForeignKey(to=Account, on_delete=models.CASCADE, related_name='operations_account')
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Withdraw: {self.amount} : {self.date_created}"

# TODO 1 - register mod

