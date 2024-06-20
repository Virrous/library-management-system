from django.shortcuts import render,redirect
# from django.contrib.auth import authenticate
# from .models import login_detail
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth import login, authenticate,logout
from .models import *
from .forms import BookForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def get_started():
    return redirect("/form")


def form(request):
    return render(request, 'form.html')

# def login_view(request):
#      if request.method == "POST":
#         username=request.POST.get('username')
#         password=request.POST.get('password')
        
#         # check if user has entered correct creditentals or not
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect("/dashboard")
           
#         else:
#             return redirect("/")
        
# def logout_view(request):
#     logout(request)
#     return redirect('/form')

def dashboard(request):
    books = Book.objects.all()
    students = Student.objects.all()
    issues = Issued_Book.objects.all()
    return render(request, 'dashboard.html',{'books':books,'students':students, 'issues':issues})

def issueBook(request):
    issues = Issued_Book.objects.all()
    return render(request, 'issueBook.html',{'issues':issues})

    
  
# def book_list(request):
#     books = Book.objects.all()
#     return render(request, 'books.html', {'books': books})

def books(request):
    
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books')  # Redirect to the same page to see the updated list
    else:
        form = BookForm()
        # print(form.errors)
        
    books = Book.objects.all()
    return render(request, 'books.html', {'books': books,'form': form})

def add_book(request):
   pass

def students(request):
    students = Student.objects.all()
    return render(request, 'student.html', {'students':students})

def reports(request):
    return render(request, 'reports.html')

