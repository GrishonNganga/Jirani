from django.shortcuts import render

from .forms import UserRegistrationForm

def index:
    form = UserRegistrationForm()


    return render(request, 'register.html', {'register_form': form})
