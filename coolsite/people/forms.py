from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import *


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Audition
        fields = ['name', 'slug', 'age','photo', 'is_published', 'capabilities', 'country']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'capabilities': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }

    def clean_capabilities(self):
        name = self.cleaned_data['name']
        if len(name) > 200:
            raise ValidationError('Длина превышает 200 символов')

        return name



class RegisterUserForm(UserCreationForm):

    username = forms.CharField(label='Login', widget = forms.TextInput(attrs={'class': 'form-input' }))
    email = forms.EmailField(label='Email',widget=forms.EmailInput(attrs={'class': 'form-input' }))
    password1 = forms.CharField(label='Password', widget= forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
