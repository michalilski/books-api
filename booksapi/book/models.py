from django.db import models

class Book(models.Model):
    isbn = models.CharField(max_length = 13, primary_key = True)
    title = models.CharField(max_length = 200)
    author = models.CharField(max_length = 50)
    genre = models.CharField(max_length = 30)

class Opinion(models.Model):
    isbn = models.ForeignKey(Book, db_column = 'isbn', related_name = 'opinions', on_delete = models.CASCADE)
    rate = models.IntegerField()
    description = models.TextField()