from django.db import models
# from django import forms

# Create your models here.
class Book(models.Model):
    FICTION = 'fiction'
    NOVELS = 'nobels'
    CALCULATIONS = 'calculation'
    COMPUTER = 'computer'
    OTHERS = 'others'

    TYPE_CHOICES = [
        (FICTION, 'Fiction'),
        (NOVELS, 'Novels'),
        (CALCULATIONS, 'Calculations'),
        (COMPUTER, 'Computer'),
        (OTHERS, 'Others'),
    ]

    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50, blank=True, null=True)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default=OTHERS)
    shelf = models.CharField(max_length=5)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.title
        

# class Student(models.Model):
#     name = models.CharField(max_length=100)
#     address = models.CharField(max_length=100)
#     email = models.EmailField(max_length=50)
#     contact = models.PositiveBigIntegerField()
    
#     def __str__(self):
#         return self.name