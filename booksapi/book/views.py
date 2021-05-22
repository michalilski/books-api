from .models import Book
from .serializers import BookSerializer
from . import serializers
import json
from django.http import HttpResponse, Http404

def get_book_by_title(request, title):
    if request.method == 'GET':
        books = Book.objects.filter(title=title)
        serializer = BookSerializer(books, many=True)
        return HttpResponse(json.dumps(serializer.data), status=200)
    return Http404()
