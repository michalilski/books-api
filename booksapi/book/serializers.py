from rest_framework import serializers
from .models import Book, Opinion

class OpinionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opinion
        fields = ['rate', 'description']

class BookSerializer(serializers.ModelSerializer):
    opinions = OpinionSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ['isbn', 'title', 'author', 'genre', 'opinions']

