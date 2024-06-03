from django.shortcuts import redirect, render
from django.urls import reverse

from users.models import User
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
    if request.method == 'POST':
        username = request.POST.get('username')
        new_password = request.POST.get('newPassword')
        confirm_new_password = request.POST.get('confirmNewPassword')

        if new_password != confirm_new_password:
            return render(request, 'reset_password.html', {
                'error_message': 'Passwords do not match.'
            })

        try:
            user = User.objects.get(username=username)
            user.set_password(new_password)  # Use the set_password method to hash the password
            user.save()
            return render(request, 'reset_password.html', {
                'success_message': 'Password reset successfully.'
            })
        except User.DoesNotExist:
            return render(request, 'reset_password.html', {
                'error_message': 'User does not exist.'
            })
    else:
        return render(request, 'reset_password.html')