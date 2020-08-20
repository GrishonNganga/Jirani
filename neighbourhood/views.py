from django.shortcuts import render
#from .forms import UserRegistrationForm #more forms imports



# Login form template
def login(request):
    #loginform = UserLoginForm()


    return render(request, "login.html")

# Signup form template
def register(request):
    #registerform = UserRegistrationForm()

    
    return render(request, "registration_form.html")


#Home page
def home(request):
    
    return render(request, "index.html")

from .forms import UserRegistrationForm

def index:
    form = UserRegistrationForm()


    return render(request, 'register.html', {'register_form': form})
