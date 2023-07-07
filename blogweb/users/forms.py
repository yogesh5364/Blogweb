from django.core import validators
from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField()
    # name          type
    password = forms.CharField(widget=forms.PasswordInput)

class SignupForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    # name          type
    password = forms.CharField(widget=forms.PasswordInput)



