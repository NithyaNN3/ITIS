from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from users.forms import RegistrationForm, LoginForm
from django.views.decorators.csrf import csrf_protect
from .models import User
from django.http import HttpResponse
import hashlib

@csrf_protect
def login(request):
    message = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.get(username=username)
        user_password = user.password
        passwd = hashlib.sha256(user_password.decode()).hexdigest()
        # user = authenticate(
        #     username=request.POST.get('username'),
        #     password=request.POST.get('password'),
        # )
        # print("hashed_password: ", hashed_password)
        if passwd == password:
            login(request, user)
            # message = f'Hello {user.username}! You have been logged in'
            return redirect('search') 
        elif User.DoesNotExist:
            return HttpResponse("User does not exist", status=401)
        else:
            message = 'Login failed!'
            return HttpResponse("Invalid credentials", status=401)
    else:
        form = LoginForm()
    return render(request, 'login.html', context={'form': form, 'message': message})

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def reset_password(request):
    return render(request, 'reset_password.html')