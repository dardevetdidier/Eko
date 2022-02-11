from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Deposit(models.Model):
    description = models.CharField(max_length=150)
    amount = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"Deposit: {self.amount} : {self.date_created}"



class Withdraw(models.Model):
    description = models.CharField(max_length=150)
    amount = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Withdraw: {self.amount} : {self.date_created}"


class Account(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    balance = models.FloatField()
    deposit = models.ForeignKey(to=Deposit, on_delete=models.CASCADE)
    withdraw = models.ForeignKey(to=Withdraw, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# TODO 1 - register mod

