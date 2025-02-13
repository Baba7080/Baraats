from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    City = forms.CharField(max_length=100)
    class Meta:
        model = User
        fields = ['username','email','City','password1','password2']


class UserUpdateForms(forms.ModelForm):
    email= forms.EmailField()
    City = forms.CharField()

    class Meta:
        model = User
        fields = ['username','email','City']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:

        model = Profile
        fields = ['image']