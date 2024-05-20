from django.shortcuts import render, redirect
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from django.contrib.auth import authenticate, login
# from django.contrib import messages
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer, LoginSerializer
from django.core.validators import ValidationError
from rest_framework.authtoken.models import Token
# from .forms import UserRegisterForm

# def register(request):
#     if request.method == "POST":
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get("username")
#             messages.success(request, f"Account created for {username}!")
#             return redirect("library-home")
#     else:
#         form = UserRegisterForm()
#     return render(request, "users/register.html", {"form": form})

@api_view(['POST'])
@parser_classes([JSONParser])
def register(request):
    if request.method == "POST":
        # username = request.POST.get("username","").strip()
        # email = request.POST.get("email","").strip()
        # password = request.POST.get("password","").strip()
        serializer = RegisterSerializer(data = request.data)
        # if username and password 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# @api_view(['POST'])
# def login(request):
#     # Logic for authenticating user and returning token
#     # if request.data.get("email") != "":
#     username = request.data.get("username")
#     # else:
#     #     username = request.data.get("username")
#     password = request.data.get("password")
#     serializer = LoginSerializer(data=request.data)
#     # if serializer.is_valid():
    
#     # if email != "":
#     user = authenticate(request, username = username, password = password)
#     # else:
#     #     user = authenticate(request, username = username, password = password)

#     if user is not None:
#         # Token.objects.get_or_create(user = user)
#         return Response("Login successful", status=status.HTTP_200_OK)
#     else:
#         return Response({"error": "Invalid Credentials"}, status=status.HTTP_400_BAD_REQUEST)
    

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




# myapp/views.py
# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from django.contrib.auth import authenticate
# from rest_framework.authtoken.models import Token
# from .serializers import UserSerializer

# @api_view(['POST'])
# def register(request):
#     serializer = UserSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['POST'])
# def login(request):
#     username = request.data.get('username')
#     password = request.data.get('password')
    
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({'token': token.key}, status=status.HTTP_200_OK)
#     else:
#         return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)


