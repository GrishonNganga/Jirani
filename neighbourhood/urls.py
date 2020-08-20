from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'login$', views.logIn, name='login'),
    url(r'^$', views.home, name='home'),
    url(r'register$', views.register, name='register'),
    url(r'announce/(\d+)', views.announcement, name='announce'),
    url(r'announce/new/', views.create_announcement, name='new-announcement'),
    url(r'^profile$', views.profile, name='profile'),
    url(r'announce/', views.announcement, name='announce'),
    url(r'blog/', views.blog, name='blog'),
    url(r'business/(\d+)', views.business, name='business'),
    url(r'business/new/', views.create_business, name='add-business'),
    url(r'essential/', views.essential, name='essential'),
    url(r'meeting/', views.meeting, name='meeting'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
