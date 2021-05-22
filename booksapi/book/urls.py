from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('find/title/<str:title>', views.get_book_by_title)
]
