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