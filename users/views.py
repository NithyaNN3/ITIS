from django.shortcuts import redirect, render

from users.forms import RegistrationForm


def login(request):
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login/')  
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def reset_password(request):
    return render(request, 'reset_password.html')