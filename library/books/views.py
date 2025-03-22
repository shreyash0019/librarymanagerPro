from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Book, BorrowedBook, Student
from .forms import BookForm, SignupForm
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect  # Ensure CSRF is enabled

# Home Page (Handles Student Login)
def home(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('student_dashboard')  # Redirect to student dashboard after login
        else:
            return render(request, 'home.html', {'error': 'Invalid username or password'})

    return render(request, 'home.html')

# Student Signup
def student_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

# Admin Login

@csrf_protect

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')  # Use `.get()` with a default value
        password = request.POST.get('password', '')

        if not username or not password:
            return render(request, 'admin_login.html', {'error': 'Username and password are required'})

        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('admin_dashboard')  # Redirect to admin dashboard
        else:
            return render(request, 'admin_login.html', {'error': 'Invalid credentials'})

    return render(request, 'admin_login.html')

# Admin Dashboard
@login_required
def admin_dashboard(request):
    if not request.user.is_superuser:
        return redirect('home')

    books = Book.objects.all()
    return render(request, 'admin_dashboard.html', {'books': books})

# Add Book (Admin)
@login_required
def add_book(request):
    if not request.user.is_superuser:
        return redirect('home')

    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})

# Edit Book (Admin)
@login_required
def edit_book(request, book_id):
    if not request.user.is_superuser:
        return redirect('home')

    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = BookForm(instance=book)
    return render(request, 'edit_book.html', {'form': form, 'book': book})

# Delete Book (Admin)
@login_required
def delete_book(request, book_id):
    if not request.user.is_superuser:
        return redirect('home')

    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('admin_dashboard')
    return render(request, 'delete_book.html', {'book': book})

# Student Dashboard (View Available Books)
@login_required
def student_dashboard(request):
    books = Book.objects.filter(quantity__gt=0)  # Only show books with quantity > 0
    return render(request, 'student_dashboard.html', {'books': books})

# Borrow Book
@login_required
def borrow_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    student = get_object_or_404(Student, user=request.user)

    if book.quantity > 0:
        # Reduce the book quantity
        book.quantity -= 1
        book.save()

        # Create a borrowed book entry
        BorrowedBook.objects.create(student=student, book=book)

        return redirect('student_dashboard')  # Redirect back to student dashboard

    return render(request, 'student_dashboard.html')  # Show an error page if unavailable

# View Borrowed Books (Student)
@login_required
def borrowed_books(request, student_id):  # Accept student_id
    student = get_object_or_404(Student, id=student_id)
    borrowed_books = BorrowedBook.objects.filter(student=student)
    print(borrowed_books)  # Debugging line
    return render(request, 'borrowed_books.html', {'borrowed_books': borrowed_books})

@login_required
def return_book(request, borrowed_book_id):
    borrowed_book = get_object_or_404(BorrowedBook, id=borrowed_book_id, student__user=request.user)

    if request.method == "POST":
        # Increase the quantity of the book
        book = borrowed_book.book
        book.quantity += 1
        book.save()
        
        # Get the student ID before deleting the record
        student_id = borrowed_book.student.id
        
        # Remove the borrowed book record
        borrowed_book.delete()

        # Redirect with student_id
        return redirect('borrowed_books', student_id=student_id)

    # If accessed via GET, redirect properly
    return redirect('borrowed_books', student_id=borrowed_book.student.id)


# Logout
def user_logout(request):
    logout(request)
    return redirect('home')


from rest_framework import viewsets, permissions
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .models import Book, BorrowedBook, Student
from .serializers import UserSerializer, StudentSerializer, BookSerializer, BorrowedBookSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

class BorrowedBookViewSet(viewsets.ModelViewSet):
    queryset = BorrowedBook.objects.all()
    serializer_class = BorrowedBookSerializer
    permission_classes = [permissions.IsAuthenticated]

from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token  # Ensure this is imported
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['POST'])
def api_admin_login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)

    if user is not None and user.is_superuser:
        token, _ = Token.objects.get_or_create(user=user)  # Correct way to access Token
        return Response({'token': token.key, 'message': 'Admin login successful'})

    return Response({'error': 'Invalid credentials'}, status=400)

