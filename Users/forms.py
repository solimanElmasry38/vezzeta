from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import *

class CreateNewUser(UserCreationForm):
    class Meta:
        model = User 
        fields =['email','first_name','last_name','password1','password1','username']
        error_messages = {
            'password1': {
                'required': ('Please enter a password.')
            },
            'password2': {
                'required': ('Please enter a password.')
            }}


class EditeUserInfoForm(forms.ModelForm):
    class Meta:
        model = User 
        fields =['email','first_name','last_name']
    
class EditeProfileInfoForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields =['img','phone','are_you_doctor']
    


class AddsForm(ModelForm):
    def create (un,self):
        self.user = un

     
    class Meta:

        model = Add
        fields = "__all__"
    
