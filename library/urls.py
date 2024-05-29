from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name = "library-home"),
    path("about/", views.about, name = "library-about"),
    path("books", views.list_book, name = "list_book"),
    path("book/add", views.add_book, name = "add_book"),
    path("book/<int:pk>/", views.book_detail, name = "book_detail"),
]