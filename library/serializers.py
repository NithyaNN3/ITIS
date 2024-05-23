from rest_framework import serializers
from django.utils import timezone
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=100)
    author = serializers.CharField(max_length=100)
    content = serializers.CharField()
    date_added = serializers.FloatField()

    class Meta:
        model = Book
        fields = ["title", "author", "content", "date_added"]


"""
convert published date to epoch timestamp, change fieldname?
add and test register & login urls
test negative cases (invalid inputs, etc)
"""