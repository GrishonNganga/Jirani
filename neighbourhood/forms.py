<<<<<<< HEAD
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User
=======
from django.contrib.auth.forms import UserCreationForm
from .models import User,Business
from django import forms
>>>>>>> e112882bbbec96c70b951a281175589734ee2d69

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class AddBizForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ['name','email','description']        