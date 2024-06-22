from email.utils import parsedate
from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from .models import *
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    return render(request, 'index.html')

def get_started():
    return redirect("/form")


def form(request):
    if request.method=='POST':
        if 'register' in request.POST:
            username = request.POST.get('username')
            email = request.POST.get('email')
            passwd = request.POST.get('pswd')
            my_user = User.objects.create_user(username,email,passwd)
            my_user.save()
            # print(username,email,password)
            return redirect('form')
        
        elif 'login' in request.POST:
            login_username = request.POST.get('login_username')
            password1 = request.POST.get('password')
            re_password = request.POST.get('re_password')
            # if password != re_password:
            #     return redirect('form')
            user = authenticate(request,username=login_username,password=password1)
            # print (f"value of user {user}") # type: ignore
            if user is not None:
                login(request,user)
                return redirect('dashboard')
            else:
                return redirect('form')
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
    if request.method=="POST":
        if 'add_another' in request.POST:
            book_id = request.POST.get('book_id')
            student_id = request.POST.get('student_id') 
            issue_date = request.POST.get('issue_date')
            return_date = request.POST.get('return_date')
            issue_date = parsedate(issue_date)
            book = Book.objects.get(id=book_id)
            student = Student.objects.get(id=student_id)
            issued_book = Issued_Book(book=book, student=student,issue_date=issue_date,return_date=return_date)
            # print(issued_book)
            issued_book.save()
            book.quantity -=1
            book.save()
            
        elif 'delete_issue' in request.POST:
                student_id = request.POST.get('student_id')
                student = get_object_or_404(Student, id=student_id)
                student.delete()
        elif 'query' in request.POST:
                query = request.POST.get('query')
                issues = Issued_Book.objects.filter(book__title__icontains=query) | Issued_Book.objects.filter(student__name__icontains=query)
                books = Book.objects.all()
                students = Student.objects.all()
                return render(request, 'issueBook.html',{'issues':issues,'books':books,'students':students})
            
    books = Book.objects.all()
    students = Student.objects.all()
    issues = Issued_Book.objects.all()
    return render(request, 'issueBook.html',{'issues':issues,'books':books,'students':students})

# @csrf_exempt
def books(request):
    if request.method == 'POST':
            # Handle form submissions for adding/searching books
            if 'add_another' in request.POST:
                title = request.POST.get('title')
                author = request.POST.get('author')
                type = request.POST.get('types')
                shelf = request.POST.get('shelf')
                quantity = request.POST.get('quantity')
                book_item = Book(title=title, author=author, type=type, shelf=shelf, quantity=quantity)
                book_item.save()
                
            elif 'delete_book' in request.POST:
                book_id = request.POST.get('book_id')
                book = get_object_or_404(Book, id=book_id)
                book.delete()
            
            elif 'query' in request.POST:
                query = request.POST.get('query')
                books = Book.objects.filter(title__icontains=query)
                return render(request, 'books.html', {'books': books})

    books = Book.objects.all()
    return render(request, 'books.html', {'books': books})


def add_book(request):
   pass

def students(request):
    try:
        if request.method == 'POST':
            if 'add_another' in request.POST:
                name1 = request.POST.get('name')
                address1 = request.POST.get('address')
                contact1 = request.POST.get('contact')
                email1 = request.POST.get('email')
                # print(name1,address1,contact1,email1)
                student_item = Student(name=name1, address=address1,email=email1,contact=contact1)
                # print(student_item)
                student_item.save()
                
            elif 'delete_student' in request.POST:
                student_id = request.POST.get('student_id')
                student = get_object_or_404(Student, id=student_id)
                student.delete()
                
            elif 'query' in request.POST:
                query = request.POST.get('query')
                students = Student.objects.filter(name__icontains=query)
                return render(request, 'student.html', {'students': students})
    except:
        pass
        
    students = Student.objects.all()
    return render(request, 'student.html', {'students':students})

def reports(request):
    return render(request, 'reports.html')

# def handle_request_data(request):
#     try:
#         name = request.POST['name']
#     except MultiValueDictKeyError:
#         name = None  # Handle the case where 'name' is not in the request.POST
#     return name
