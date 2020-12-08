from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import AbstractUser
from .models import CustomUser


class AuthenticationForm(forms.Form):
    pass


class CreateUserForm(UserCreationForm):
    

    class Meta:
        model = CustomUser
        fields = ("group", "username",'area1','area2')

    def save(self, commit=True):
        user = super(CreateUserForm, self).save(commit=False)
        user.group = self.cleaned_data["group"]
        user.area1 = self.cleaned_data["area1"]
        user.area2 = self.cleaned_data["area2"]
        
        
        if commit:
            user.save()
        return user


class UserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("group", "username",'area1','area2')

    def save(self, commit=True):
        user = super(CreateUserForm, self).save(commit=False)
        user.group = self.cleaned_data["group"]
        user.area1 = self.cleaned_data["area1"]
        user.area2 = self.cleaned_data["area2"]
        
        
        if commit:
            user.save()
        return user