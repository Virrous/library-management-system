
from django.urls import path
from main_app import  views

urlpatterns = [
     path("", views.index, name='index'),
     path("get_started", views.get_started, name='get_started'),
     path("form", views.form, name='form'),
     # path('after_login', views.after_login, name="after_login"),
     path('login', views.login_view, name="login"),
     # path('logout',views.logout_view, name='logout'),
     # path("signup", views.signup_view, name="signup"),
     path("dashboard", views.dashboard, name='dashboard'),
     path('books', views.books, name='books'),
     path('students', views.students, name='students'),
     path('issueBook', views.issueBook, name='issueBook'),
     path('reports', views.reports, name='reports'),
     path('settings', views.settings, name='settings'),
]
