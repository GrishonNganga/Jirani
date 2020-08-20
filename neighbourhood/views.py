from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserLoginForm
from .models import User
from django.contrib.auth import login, authenticate


def register(request):
    if request.method == 'POST' and register_user(request):
        return redirect('/login')    
    registerform = UserRegistrationForm()        
    return render(request, "registration_form.html", {'register_form': registerform})


def logIn(request):
    if request.method == 'POST' and request.POST.get('username') and request.POST.get('password'):
        if validate_and_login_user(request):
            return redirect('/')
        
    
    loginform = UserLoginForm()
    return render(request, 'login.html', {'login_form': loginform})


#Home page
def home(request):
    
    return render(request, "index.html")

<<<<<<< HEAD
#Profile page
def profile(request):
    
    return render(request, "profile.html")

#Announcement page
def announcement(request):
    
    return render(request, "announcement.html")

#Blog page
def blog(request):
    
    return render(request, "blog.html")

#Business page
def business(request):
    
    return render(request, "business.html")

#Essential page
def essential(request):
    
    return render(request, "essential.html")

#Meeting page
def meeting(request):
    
    return render(request, "meeting.html")
=======

def register_user(request):

    form = UserRegistrationForm(request.POST)
    if form.is_valid():
        form.save()
        return True
    else:
        return False


def check_if_user_exist(username, password):
    if username == None or password == None:
        return False
        
    return User.objects.filter(username = username).exists()

def authenticate_user(request, username, password):
    return authenticate(request, username= username, password = password)

    
def validate_and_login_user(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    user_exists = check_if_user_exist(username, password)

    if user_exists:
        user = authenticate_user(request, username, password)
    else:
        return False

    if user:
        login(request, user)
        
        return True
        
        
>>>>>>> grishon1
