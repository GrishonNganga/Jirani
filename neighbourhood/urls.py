from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
<<<<<<< HEAD
    url(r'login$', views.logIn, name='login'),
=======
    url(r'^$', views.home, name='home'),
    url(r'login$', views.login, name='login'),
>>>>>>> e112882bbbec96c70b951a281175589734ee2d69
    url(r'register$', views.register, name='register'),
    url(r'announce/', views.announcement, name='announce'),
    url(r'blog/', views.blog, name='blog'),
    url(r'business/', views.business, name='business'),
    url(r'new/business/', views.create_business, name='add-business'),
    url(r'essential/', views.essential, name='essential'),
    url(r'meeting/', views.meeting, name='meeting'),
    url(r'profile/', views.profile, name='profile'),
    
]