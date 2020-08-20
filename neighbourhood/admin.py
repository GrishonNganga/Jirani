from django.contrib import admin
from .models import User, Business, Hood
 
admin.site.register(User)
admin.site.register(Hood)
admin.site.register(Business)