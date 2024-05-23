from django.shortcuts import render, redirect
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer, LoginSerializer
from django.core.validators import ValidationError
from rest_framework.authtoken.models import Token

@api_view(['POST'])
@parser_classes([JSONParser])
def register(request):
    if request.method == "POST":
        serializer = RegisterSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
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
            return Response({"token": token.key}, status = status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid Credentials"}, status = status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)



