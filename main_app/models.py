from django.db import models
# from django import forms

# Create your models here.
class login_detail(models.Model):
    username=models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    password=models.CharField(max_length=16)
    
    def __str__(self):
        return self.username
        
# class user_info(login_detail):
#     firstname = models.CharField(max_length=30, blank=True)
#     lastname  = models.CharField(max_length=30, blank=True