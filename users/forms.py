from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()


class Sign_up_form(forms.Form):

    username = forms.CharField(label='Username', max_length=32, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username'
    }))

    email = forms.EmailField(label='Email',widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email'
    }))

    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password'
    }))

    confirm_password = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Confirm Password'
    }))

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            User.objects.get(username=username)
            raise ValidationError('username exists')
        except User.DoesNotExist:
            return username

    def clean(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            # raise ValidationError('password do not match')
            self.add_error('password', 'Password do not match')
            self.add_error('confirm_password', 'Password do not match')

    def save(self):
        del self.cleaned_data['confirm_password']
        User.objects.create_user(**self.cleaned_data)


class Sign_in_form(forms.Form):
    username = forms.CharField(label='Username', max_length=32, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username'
    }))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password'
    }))