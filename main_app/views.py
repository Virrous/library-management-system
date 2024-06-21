from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from .models import *
from .forms import BookForm

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
                return HttpResponse ('incorrect!!')
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
            return redirect('/books')  # Redirect to the same page to see the updated list
    else:
        form = BookForm()
        # print(form.errors)
        
    books = Book.objects.all()
    return render(request, 'books.html', {'books': books,'form': form})

def add_book(request):
   pass

def students(request):
    try:
        if request.method == 'POST':
            name = request.POST.get('name')
            address = request.POST.get('address')
            contact = request.POST.get('contact')
            email = request.POST.get('email')
            
            if name and address and contact and email:
                student_item = Student(name=name, address=address, contact=contact, email=email)
                student_item.save()
                return redirect('students/') 
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
