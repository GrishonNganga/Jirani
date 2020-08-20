from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [    
    url(r'^login$', views.login, name='login'),    
    url(r'^register$', views.register, name='register'),
    url(r'^$', views.home, name='home'),
    url(r'^profile$', views.profile, name='profile'),
    url(r'^announce/$', views.announcement, name='announce'),
    url(r'^blog/$', views.blog, name='blog'),
    url(r'^business/$', views.business, name='business'),
    url(r'^new/business/$', views.create_business, name='add-business'),
    url(r'^essential/$', views.essential, name='essential'),
    url(r'^meeting/$', views.meeting, name='meeting'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
