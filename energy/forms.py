from .models import Message
from django import forms
from django.contrib.auth.models import User
class MessageForm(forms.ModelForm):
        class Meta:
            model=Message
            fields=['title','content','img','type']

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model=User
        fields=['username','email','password']