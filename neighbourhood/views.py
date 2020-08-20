from django.shortcuts import render
from .forms import UserRegistrationForm #more forms imports



# Login form template
def login(request):
    loginform = UserLoginForm()


    return render(request, "login.html", {"loginform" : loginform})

# Signup form template
def register(request):
    registerform = UserRegistrationForm()

    
    return render(request, "registration_form.html", {"registerform" : registerform})


#Home page
def home(request):
    
    return render(request, "index.html")

