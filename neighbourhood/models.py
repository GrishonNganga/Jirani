from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_admin = models.BooleanField(default=False)

class Hood(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    population = models.CharField(max_length=100)
    admin = models.ManyToManyField(User) 

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
