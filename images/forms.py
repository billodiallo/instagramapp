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

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude =['poster','image']

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
       