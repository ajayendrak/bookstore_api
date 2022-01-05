from django.urls import path
from .views import *
from django.views.decorators.csrf import csrf_exempt



urlpatterns=[
	path("store-list", StoresListAPIView.as_view(), name='store-list'),
	path("book-list/<int:pk>", BooksListAPIView.as_view(), name='book-list'),
	path("", (StoreCreateAPIView.as_view()), name='store-create'),
	path("store-edit/<int:pk>", (StoreRetriveUpdateDelete.as_view()), name='store-edit'),
	path("book-edit/<slug:pk>", (BookRetriveUpdateDelete.as_view()), name='book-edit'),

] 
