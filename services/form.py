from django.forms import ModelForm
from django.contrib.auth.forms import   UserCreationForm
from django import forms
from django.contrib.auth.models import User

class FormDangKy(UserCreationForm):
    class meta:
        moddel=User
        fields=['username','email','password1','password2']