from rest_framework import serializers

from .models import Book, Opinion


class OpinionSerializer(serializers.ModelSerializer):
    """Serializer class for book opinion."""
    class Meta:
        model = Opinion
        fields = ["rate", "description"]


class BookSerializer(serializers.ModelSerializer):
    """Serializer class for book.

    This serializer returns all book fields and all opinions
    about this book.
    """
    opinions = OpinionSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ["isbn", "title", "author", "genre", "opinions"]
