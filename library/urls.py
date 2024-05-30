from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search_results, name='search_results'),
    path('download/<str:file_name>/', views.download_file, name='download_file')
]