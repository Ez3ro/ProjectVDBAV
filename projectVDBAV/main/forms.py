from dataclasses import field
from django import forms
from django.contrib.auth.forms import UserCreationForm
from  django.contrib.auth.models import User
from main.models import TimeIn_Out
from main.models import Post
import datetime

class RegisterForm(UserCreationForm):

    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["Carname", "Platenumber", "Carcolor"]

class TimeIn(forms.ModelForm):
    class Meta:
        model = TimeIn_Out
        TimeIn =datetime.datetime.now() 
        fields = []
        

