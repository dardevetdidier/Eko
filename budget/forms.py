from django import forms

from django.contrib.auth.models import User
from .models import Account, Operation, Category


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password'
        ]

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control',
                                               'placeholder': 'Nom d\'utilisateur',
                                               }),
            'password': forms.PasswordInput(attrs={'class': 'form-control',
                                                   'placeholder': 'Mot de passe'
                                                   })
        }


class CreateAccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = [
            'name',
            'balance'
        ]

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'Nom du compte'
                                           }),
            'balance': forms.NumberInput(attrs={'class': 'form-control',
                                                'placeholder': 'Solde de départ'
                                                })
        }


class DeleteForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['name', ]

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'Nom du compte à supprimer'})
        }


class CreateOperationForm(forms.ModelForm):
    class Meta:
        model = Operation
        fields = [
            'operation_type',
            'description',
            'amount',
            'category',
            'account',
            'date_created'
        ]

        widgets = {
            'operation_type': forms.Select(attrs={'class': 'form-select'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'account': forms.Select(attrs={'class': 'form-select'}),


        }


class CreateCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', ]

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'Nom de la Catégorie'})
        }
