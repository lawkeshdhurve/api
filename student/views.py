from django.shortcuts import render
from .models import Student, Book, IssuedBook
from .models import IssuedBook

def home(request):
    issued_books = IssuedBook.objects.select_related('book', 'student').all()
    return render(request, 'student/home.html', {'issued_books': issued_books})

def all_books(request):
    books = Book.objects.all()
    return render(request, 'student/books.html', {'books': books})

def all_students(request):
    students = Student.objects.all()
    return render(request, 'student/students.html', {'students': students})
