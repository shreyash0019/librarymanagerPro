from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import UserViewSet, StudentViewSet, BookViewSet, BorrowedBookViewSet

# API Router
router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'students', StudentViewSet)
router.register(r'books', BookViewSet)
router.register(r'borrowed-books', BorrowedBookViewSet)

urlpatterns = [
    # Traditional Views
    path('', views.home, name='home'),  # Home page
    path('signup/', views.student_signup, name='student_signup'),  # Student Signup
    path('admin-login/', views.admin_login, name='admin_login'),  # Admin Login
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),  # Admin Dashboard
    path('add-book/', views.add_book, name='add_book'),  # Add Book
    path('edit-book/<int:book_id>/', views.edit_book, name='edit_book'),  # Edit Book
    path('delete-book/<int:book_id>/', views.delete_book, name='delete_book'),  # Delete Book
    path('dashboard/', views.student_dashboard, name='student_dashboard'),  # Student Dashboard
    path('borrow/<int:book_id>/', views.borrow_book, name='borrow_book'),  # Borrow Book
    path('borrowed-books/<int:student_id>/', views.borrowed_books, name='borrowed_books'),
    path('return/<int:borrowed_book_id>/', views.return_book, name='return_book'),  # Return Book
    path('logout/', views.user_logout, name='logout'),  # Logout
    
    # API Endpoints
    path('api/', include(router.urls)),
]
from django.urls import path
from .views import api_admin_login

urlpatterns += [
    path('api/admin-login/', api_admin_login, name='api_admin_login'),
]
