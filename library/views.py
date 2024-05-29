import os
import boto3
from django.http import HttpResponse, Http404
from botocore.exceptions import NoCredentialsError
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
    
def search_results(request):
    query = request.GET.get('q')
    results = []

    if query:
        s3 = boto3.client('s3')
        bucket_name = 'libraryassignment2bucket'

        # List objects in the specified S3 bucket
        try:
            response = s3.list_objects_v2(Bucket=bucket_name)
            for obj in response.get('Contents', []):
                file_name = obj['Key']
                if file_name.endswith('.txt') and query.lower() in file_name.lower():
                    results.append(file_name)
        except NoCredentialsError:
            return HttpResponse("AWS credentials not found.", status=500)
        except Exception as e:
            return HttpResponse(f"Error: {str(e)}", status=500)

    return render(request, 'search.html', {'results': results, 'query': query})

def download_file(request, file_name):
    s3 = boto3.client('s3')
    bucket_name = 'libraryassignment2bucket'

    try:
        # Download the file from S3
        s3.download_file(bucket_name, file_name, f'/tmp/{file_name}')

        # Serve the file as an HTTP response
        with open(f'/tmp/{file_name}', 'rb') as f:
            response = HttpResponse(f.read(), content_type='application/octet-stream')
            response['Content-Disposition'] = f'attachment; filename="{file_name}"'
            return response

    except NoCredentialsError:
        return HttpResponse("AWS credentials not found.", status=500)
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}", status=500)