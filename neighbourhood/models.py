from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_admin = models.BooleanField(default=False)

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
    hood = models.ForeignKey(Hood, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profiles/')