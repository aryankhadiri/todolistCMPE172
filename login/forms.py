"""
This file contains forms used for user login.
"""

# -----------------------------------------------------------------------------------------------------------------------------------------
#       IMPORTS                 
# -----------------------------------------------------------------------------------------------------------------------------------------
from django import forms
from .models import User
from django.core.validators import EmailValidator

# -----------------------------------------------------------------------------------------------------------------------------------------
#       LOGIN FORM          
# -----------------------------------------------------------------------------------------------------------------------------------------
class LoginForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'id': 'email',
        'placeholder': 'Email...',
    }), validators=[EmailValidator()])

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'id': 'password',
        'placeholder': 'Password...',
    }))
    firstname = forms.CharField(widget=forms.TextInput(attrs={
        'id': 'fname',
        'placeholder': 'Firstname',
    }))
    lastname = forms.CharField(widget=forms.TextInput(attrs={
        'id': 'lname',
        'placeholder': 'Lastname',
    }))
    class Meta:
        model = User
        fields = {
            'email',
            'password',
            'firstname',
            'lastname',
        }
    def save(self, commit = True):
        user = super(LoginForm, self).save(commit = False)
        user.set_password(self.cleaned_data["password"])
        user.admin = False
        if commit:
            user.save()
        return user