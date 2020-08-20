from django.shortcuts import render
from .forms import UserRegistrationForm 


def register(request):
    registerform = UserRegistrationForm()

    return render(request, "registration_form.html", {'register_form': registerform})


def login(request):
    return render(request, 'login_form.html')


#Home page
def home(request):
    
    return render(request, "index.html")
