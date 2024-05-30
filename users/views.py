from django.shortcuts import render, redirect
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer, LoginSerializer, PasswordSerializer
from django.core.validators import ValidationError
from rest_framework.authtoken.models import Token
from django.http import HttpResponse, Http404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

@api_view(['POST'])
@parser_classes([JSONParser])
def register(request):
    try:
        if request.method == "POST":
            serializer = RegisterSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                messages.success(request, f'Account created for {request.data.get('username')}!')
                # return redirect('library-home')
                return render(request, 'search.html', status=status.HTTP_200_OK)
            else:
                return render(request, 'users/ITIS.html', {'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)
        else:
            # Handle other HTTP methods if needed
            return render(request, 'users/ITIS.html', status=status.HTTP_405_METHOD_NOT_ALLOWED)
    except Exception as e:
        return render(request, 'users/ITIS.html', {'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['POST'])
def login(request):
    serializer = LoginSerializer(data = request.data)
    if serializer.is_valid():
        username = serializer.validated_data["username"]
        password = serializer.validated_data["password"]
        user = authenticate(request, username = username, password = password)
        print("user: ", user)
        if user is not None:
            token, _ = Token.objects.get_or_create(user = user)
            # return Response({"token": token.key}, status = status.HTTP_200_OK)
            return render(request,
                          'search.html',
                          status = status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid Credentials"}, status = status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@parser_classes([JSONParser])
def password_reset(request):
    if request.method == "PUT":
        serializer = PasswordSerializer(data = request.data)
        if serializer.is_valid():
            serializer.update(None, serializer.validated_data)
            return Response("Password updated successfully", status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
