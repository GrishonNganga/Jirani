from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'login$', views.login, name='login'),
    url(r'register$', views.register, name='register'),
    url(r'announce/(\d+)', views.announcement, name='announce'),
    url(r'announce/new/', views.create_announcement, name='new-announcement'),
    url(r'blog/', views.blog, name='blog'),
    url(r'business/(\d+)', views.business, name='business'),
    url(r'business/new/', views.create_business, name='add-business'),
    url(r'essential/', views.essential, name='essential'),
    url(r'meeting/', views.meeting, name='meeting'),
    url(r'profile/', views.profile, name='profile'),
    
]