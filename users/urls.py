# users/urls.py

from django.urls import path
from .views import login, register, reset_password

urlpatterns = [
    path('register/', register, name='register'),
    path('', login, name='login'),
    path('reset-password/', reset_password, name='reset-password')
]
