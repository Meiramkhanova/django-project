from django import forms
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
