from django import forms
from django.contrib.auth.forms import UserCreationForm *

class NewProfile(forms.ModelForm):
    class Meta:
        model = Profile 
        exclude = ['user']

class UploadForm(forms.Models):
    class Meta:
        model = Profile
        exclude = ['user']

