from django import forms

from django.contrib.auth.models import User
from .models import Account, Operation


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
            'description',
            'amount',
            'category',
            'account'
        ]

        widgets = {
            'description': forms.TextInput(attrs={'class': 'form-control',
                                                  'placeholder': 'Description'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control',
                                               'placeholder': 'Montant'}),
            'category': forms.TextInput(attrs={'class': 'form-control',
                                               'placeholder': 'Catégorie'}),
            'account': forms.TextInput(attrs={'class': 'form-control',
                                              'placeholder': 'Compte'}),
        }
