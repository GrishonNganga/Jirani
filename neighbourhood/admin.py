from django.contrib import admin
from .models import User, Business, Hood, Announcement, Profile
 
admin.site.register(User)
admin.site.register(Hood)
admin.site.register(Business)
admin.site.register(Announcement)
admin.site.register(Profile)
