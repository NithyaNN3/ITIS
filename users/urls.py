# users/urls.py

from django.urls import path
from .views import login, register, reset_password

urlpatterns = [
    path('login/register/', register, name='register'),
    path('login/', login, name='login'),
    path('login/reset_password/', reset_password, name='reset_password')
]
