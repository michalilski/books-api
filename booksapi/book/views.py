from .models import Book
from .serializers import BookSerializer
import json
from django.http import HttpResponse, HttpResponseBadRequest

def get_book_by_title(request):
    if request.method == 'GET':
        title = request.GET.get('title', '')
        if title == '':
            books = []
        else:
            books = Book.objects.filter(title__startswith=title)
        serializer = BookSerializer(books, many=True)
        return HttpResponse(json.dumps(serializer.data, indent=4), 
        content_type='application/json; charset=utf-8', 
        status=200)
    return HttpResponseBadRequest()
