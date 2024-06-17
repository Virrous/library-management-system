from django.db import models
# from django import forms

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    
    # for book type
    fiction = 'fiction'
    nobels = 'nobels'
    calculation = 'calculation'
    computer = 'computer'
    others = 'others'
    type_choice = [
        (fiction, 'fiction'),
        (nobels, 'nobels'),
        (calculation, 'calculation'),
        (computer, 'computer'),
        (others, 'others'),
    ]
    type = models.CharField(max_length=20,choices=type_choice,default=others)
    shelf = models.CharField(max_length=5)
    quantity = models.PositiveIntegerField()
    
    # to define models name in database
    def __str__(self):
        return self.title
        

class Student(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    contact = models.PositiveBigIntegerField()
    
    def __str__(self):
        return self.name