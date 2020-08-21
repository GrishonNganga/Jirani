from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    picture = models.ImageField(default='profiles/default.jpg', upload_to='profiles/')

class Hood(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    population = models.CharField(max_length=100)
    admin = models.ManyToManyField(User) 
    

    @classmethod
    def get_all_hoods(cls):
        return(Hood.objects.all())

class Business(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    description = models.TextField()
    hood = models.ForeignKey(Hood, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    @classmethod
    def filter_by_hood(cls,id):
        businesses = cls.objects.filter(hood_id = id)
        return businesses

class Announcement(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    hood = models.ForeignKey(Hood, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    @classmethod
    def filter_by_hood(cls,id):
        news = cls.objects.filter(hood_id = id)
        return news


class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    hood = models.ForeignKey(Hood, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    @classmethod
    def filter_by_hood(cls,id):
        news = cls.objects.filter(hood_id = id)
        return news


class Profile(models.Model):
    name = models.CharField(max_length=50, default='')
    location = models.CharField(max_length=100, default='')
    neighbourhood = models.CharField(max_length=250, default='')
    user = models.OneToOneField(User, on_delete=models.CASCADE) 

    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, name=instance.get_full_name(), location='', neighbourhood='')

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
