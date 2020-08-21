from django.shortcuts import render, redirect
from .forms import AddBizForm,AnnouncementForm,UserRegistrationForm 
from .models import User, Business,Announcement, Blog,Essential,Meeting
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate

from .forms import UserRegistrationForm, UserLoginForm, AddBizForm
from .models import User, Hood, Business

def register(request):
    if request.method == 'POST' and register_user(request):
        return redirect('/login')    
    registerform = UserRegistrationForm()        
    return render(request, "registration_form.html", {'register_form': registerform})

def logIn(request):
    if request.method == 'POST' and request.POST.get('username') and request.POST.get('password'):
        if validate_and_login_user(request):
            return redirect('/profile')
    loginform = UserLoginForm()
    return render(request, 'login.html', {'login_form': loginform})

@login_required(login_url='/login')
def home(request):
    hoods = Hood.get_all_hoods()
    return render(request, "index.html", {'hoods': hoods})


@login_required(login_url='/login')
def profile(request):
    if request.method == 'POST' and change_profile_picture(request):
        return redirect('/profile') # To access the profile image of the user -> user.picture.url
    elif request.method == 'POST' and change_profile(request):
        return redirect('/profile')
        
    user = request.user
    return render(request, 'profile.html', {'user': user})




def change_profile_picture(request):
    profile_image = request.FILES.get('profile')
    if profile_image:
        user.picture = profile_image
        user.save()
        return True
    else:
        return False


def change_profile(request):
    name = request.POST.get('name')
    location = request.POST.get('location')
    neighbourhood = request.POST.get('neighbourhood')
    if name and location and neighbourhood:
        user = request.user
        user.profile.name = name
        user.profile.location = location
        user.profile.neighbourhood = neighbourhood
        user.save()
        return True
    
    return False

    

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
    return render(request, "index.html")

#Announcement page
def announcement(request):
    news = Announcement.objects.all()     
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
    blogs = Blog.objects.all()
    return render(request, "blog.html", {'blogs': blogs})

#Business page
def business(request):
    biznas = Business.objects.all()
    return render(request, "business.html",{"biznas":biznas})

def create_business(request):
    current_user = request.user
    if request.method == 'POST' and current_user.is_admin == True:
        form = AddBizForm(request.POST, request.FILES)
        if form.is_valid():
            biz = form.save(commit=False)
            biz.user = current_user
            biz.hood = current_user.profile.neighbourhood
            biz.save()
        return redirect('index')    
    else:
        form = AddBizForm
    return render(request, 'new-biz.html', {'form':form})        

#Essential page
def essential(request):
    essentials = Essential.objects.all()
    return render(request, "essential.html",{'essentials':essentials})

#Meeting page
def meeting(request):
    meetings = Meeting.objects.all()
    return render(request, "meeting.html", {'meetings':meetings})

def search_results(request):

    if 'business' in request.GET and request.GET["business"]:
        search_term = request.GET.get("business")
        searched_businesses = Business.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'business.html',{"message":message,"businesses": searched_businesses})

    else:
        message = "You haven't searched for any term"
        return render(request, 'business.html',{"message":message})