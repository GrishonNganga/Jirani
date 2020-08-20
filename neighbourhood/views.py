from django.shortcuts import render,redirect
from .forms import AddBizForm,AnnouncementForm,UserRegistrationForm 
from .models import Business,Announcement

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
def announcement(request,hood_id):
    news = Announcement.filter_by_hood(hood_id)     
    return render(request, "announcement.html",{"news":news})

def create_announcement(request):
    current_user = request.user
    if request.method == 'POST':
        form = AnnouncementForm(request.POST, request.FILES)
        if form.is_valid():
            announcement = form.save(commit=False)
            announcement.user = current_user
            announcement.save()
        return redirect('index')    
    else:
        form = AddBizForm
    return render(request, 'new-announcement.html', {'form':form})   

#Blog page
def blog(request):
    
    return render(request, "blog.html")

#Business page
def business(request,hood_id):
    biznas = Business.filter_by_hood(hood_id)
    return render(request, "business.html",{"biznas":biznas})

def create_business(request):
    current_user = request.user
    if request.method == 'POST':
        form = AddBizForm(request.POST, request.FILES)
        if form.is_valid():
            biz = form.save(commit=False)
            biz.user = current_user
            biz.save()
        return redirect('index')    
    else:
        form = AddBizForm
    return render(request, 'new-biz.html', {'form':form})        

#Essential page
def essential(request):
    
    return render(request, "essential.html")

#Meeting page
def meeting(request):
    
    return render(request, "meeting.html")