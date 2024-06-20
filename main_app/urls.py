
from django.urls import path
from main_app import  views


urlpatterns = [
     path("", views.index, name='index'),
     
     path("get_started/", views.get_started, name='get_started'),
     
     path("form/", views.form, name='form'),
     
     path("dashboard/", views.dashboard, name='dashboard'),
     
     path('books/', views.books, name='books'),
     
    #  path('book_list', views.book_list, name='book_list'),
     path('add/', views.add_book, name='add_book'),
      
     path('students/', views.students, name='students'),
     
     path('issueBook/', views.issueBook, name='issueBook'),
     
     path('reports/', views.reports, name='reports'),
     
     path('settings/', views.settings, name='settings'),
     
]
