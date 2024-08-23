from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book

def index(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', {'books': books})

def view(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'books/view.html', {'book': book})
