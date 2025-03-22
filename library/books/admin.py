from django.contrib import admin
from .models import Book, BorrowedBook, Student  # Import your models

# Register models
admin.site.register(Book)
admin.site.register(BorrowedBook)
admin.site.register(Student)
