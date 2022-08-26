from django.contrib.auth import models
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from django.forms import fields
from home.models import Feedback

class feedback(forms.ModelForm):
    class Meta:
        model=Feedback
        fields = ['name','email','comments']