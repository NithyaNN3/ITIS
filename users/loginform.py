import hashlib
from django import forms
from .models import User

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                raise forms.ValidationError("Invalid username or password")

            entered_password_hashed = hashlib.sha256(password.encode()).hexdigest()

            if user.password != entered_password_hashed:
                raise forms.ValidationError("Invalid username or password")

        return cleaned_data