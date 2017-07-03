from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from .models import *


class Post_Form(ModelForm):
    class Meta:
        model = Post
        fields = ['content']

class Topic_Creation_Form(forms.Form):
    name = forms.CharField(max_length=50)
    content = forms.CharField(widget=forms.Textarea)

class User_LogIn_Form(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=255, widget=forms.PasswordInput)

class User_Register_Form(forms.Form):
    username = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=255)
    password = forms.CharField(max_length=255, widget=forms.PasswordInput)
    password_rep = forms.CharField(max_length=255, widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).count():
            raise forms.ValidationError("Username is already taken.")
        return username

    def clean(self):
        cleaned_data = super(User_Register_Form, self).clean()
        if cleaned_data['password'] != cleaned_data['password_rep']:
            raise forms.ValidationError("Passwords don't match")