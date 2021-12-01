from django import forms
from django.contrib.auth.forms import UserCreationForm
from account.models import User

class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=30, widget=forms.TextInput(
            attrs={
                'style': 'height:40px;',
                'placeholder' : 'Username'
            }
        ))
    email = forms.EmailField(max_length=254, widget=forms.TextInput(
            attrs={
                'style': 'height:40px;',
                'placeholder' : 'Email'
            }
        ))
    password1 = forms.CharField(max_length=32, widget=forms.PasswordInput(
            attrs={
                'style': 'height:40px;',
                'placeholder' : 'Password'
            }
        )) 
    password2 = forms.CharField(max_length=32, widget=forms.PasswordInput(
            attrs={
                'style': 'height:40px;',
                'placeholder' : 'Password confirmation'
            }
        )) 

    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')

