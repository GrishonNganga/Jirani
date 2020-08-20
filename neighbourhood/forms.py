from django.contrib.auth.forms import UserCreationForm
from .models import User,Business,Announcement
from django import forms

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserLoginForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class AddBizForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ['name','email','description'] 

class AnnouncementForm(forms.ModelForm):
    model = Announcement
    fields = ['title','content',]               