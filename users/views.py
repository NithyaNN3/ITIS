from django.shortcuts import redirect, render
from django.urls import reverse

from users.forms import RegistrationForm
from users.loginform import LoginForm


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            return redirect('library:search_results')  

    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to login page
            return redirect(reverse('users:login'))
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def reset_password(request):
    return render(request, 'reset_password.html')