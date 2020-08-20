from django.db import models

class Hood(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    population = models.CharField(max_length=100)
    #admin = models.ManyToManyField() Replace or include this after research

class Business(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    hood = models.ForeignKey(Hood, on_delete=models.CASCADE)
    #user = models.ForeignKey(User, on_delete=models.CASCADE) Include this after figuring how auth will be done.
    
