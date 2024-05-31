# users/urls.py

from django.urls import path
from .views import login

urlpatterns = [
    # path('register/', register, name='register'),
    path('login/', login, name='login'),
]
