
from django.urls import path
from main_app import  views
from django.contrib.auth.views import LogoutView


urlpatterns = [
     path("", views.index, name='index'),
     
     # path("get_started/", views.get_started, name='get_started'),
     
     path("form/", views.form, name='form'),
     
     path("dashboard", views.dashboard, name='dashboard'),
     
     path('books/', views.books, name='books'),
     path('books/<int:id>/edit/', views.books, name='edit_book'),
     
    #  path('book_list', views.book_list, name='book_list'),
     # path('add/', views.add_book, name='add_book'),
      
     path('students/', views.students, name='students'),
     
      path('students/<int:id>/edit/', views.students, name='edit_student'),
     
     path('issueBook/', views.issueBook, name='issueBook'),
     
      path('logout/', views.custom_logout, name='logout'),
]
