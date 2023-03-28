from django import forms
from .models import *

class AddPostForm(forms.Form):
    name = forms.CharField(max_length=255, label="Name")
    age = forms.CharField(max_length=255, label="Age")
    country = forms.CharField(max_length=255, label="Country")
    info_content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label="Content")
    is_published = forms.BooleanField()