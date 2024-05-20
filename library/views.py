from django.shortcuts import render
from .models import Book
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer
from datetime import datetime, timezone

# Handles traffic from the homepage
def home(request):
    context = {
        "books": Book.objects.all()
    }
    return render(request, "library/home.html", context)

def about(request):
    return render(request, "library/about.html", {"title": "About"})


# List all books in the library
@api_view(["GET", "POST"])
def list_book(request):
    if request.method == "GET":
        books = Book.objects.all()
        serializer = BookSerializer(books, many = True)
        return Response(serializer.data)

# Add a new book to the library
@api_view(["POST"])
def add_book(request):
    if request.method == "POST":
        request.data["date_added"] = datetime.now(timezone.utc).timestamp()
        serializer = BookSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# Common method to retrieve, update or delete a book
@api_view(["GET", "PUT", "DELETE"])
def book_detail(request, pk):
    try:
        book = Book.objects.get(pk = pk)
    except Book.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = BookSerializer(book)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = BookSerializer(book, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
    elif request.method == "DELETE":
        check = book.delete()
        if check == 1:
            return Response(serializer.data, status = status.HTTP_204_NO_CONTENT)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
