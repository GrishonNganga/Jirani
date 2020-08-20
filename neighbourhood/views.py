from django.shortcuts import render, redirect
from .forms import UserRegistrationForm 


def register(request):
    registerform = UserRegistrationForm()
    
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
                    
    return render(request, "registration_form.html", {'register_form': registerform})


def login(request):
    return render(request, 'login_form.html')


#Home page
def home(request):
    
    return render(request, "index.html")
