from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from .models import *
from user.models import User
from rest_framework.response import Response
from .serializers import *
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from datetime import datetime
from background_task import background


@background(schedule=60)
def Book_offer_check():
	today= datetime.today().strftime('%y-%m-%d')
	offer_book= DiscountBook.objects.all()
	for book in offer_book:
		expire= book.expiry_date.strftime('%y-%m-%d')
		if expire < today:
			book.delete()



class StoresListAPIView(ListAPIView):
	queryset = Store.objects.all()
	serializer_class = StoreSerializer
	permission_classes = [IsAuthenticated]
	pagination_class = PageNumberPagination


	def list(self, *args, **kwargs):
		queryset = self.get_queryset()
		# page = self.request.query_params.get('page')
		# if page is not None:
		# 	paginate_queryset = self.paginate_queryset(queryset)
		# 	serializer = self.serializer_class(paginate_queryset, many=True)
		# 	return self.get_paginated_response(serializer.data)
		serializer = StoreSerializer(queryset, many=True)
		return Response(serializer.data)



class StoreCreateAPIView(APIView):
	serializer_class = StoreSerializer
	permission_classes = [IsAuthenticated]

	def post(self, request):
		user_obj = get_object_or_404(User, email=request.user.email)
		owner=user_obj
		storename=request.data['storename']
		storeimage=request.data['storeimage']

		store_obj=Store(owner=owner, storename=storename, storeimage=storeimage)
		store_obj.save()

		return Response({"Store create" : "Successfully"})


class StoreRetriveUpdateDelete(APIView):
	serializer_class = StoreSerializer
	permission_classes = [IsAuthenticated]

	def get_object(self, pk):
		try:
			return Store.objects.get(pk=pk)
		except Book.DoesNotExist:
			raise Http404

	def get(self, request, pk):
		store_obj= self.get_object(pk)
		serializer= StoreSerializer(store_obj)
		return Response (serializer.data)

	def put(self, request, pk):
		store_obj=self.get_object(pk)
		user_obj = get_object_or_404(User, email=request.user.email)
		if Store.owner == user_obj:
			serializer=StoreSerializer(store_obj, request.data)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data)
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		return Response ({ "error": "You have no authority to update this Store"})


	def delete(self, request, pk):
		store_obj=self.get_object(pk)
		user_obj = get_object_or_404(User, email=request.user.email)
		if Store.owner == user_obj:
			store_obj.delete()
			return Response(status=status.HTTP_204_NO_CONTENT)
		return Response ({ "error": "You have no authority to delete this Store"})
		



class BooksListAPIView(ListAPIView):

	serializer_class = BooksSerializer
	permission_classes = [IsAuthenticated]
	pagination_class = PageNumberPagination


	
	def get(self, request, pk):
		store_obj = get_object_or_404(Store, pk=pk)
		books_obj = Books.objects.filter(from_store=store_obj)
		serializer = BooksSerializer(books_obj, many=True)
		return Response(serializer.data)
		


class BookRetriveUpdateDelete(APIView):
	serializer_class = BooksSerializer
	permission_classes = [IsAuthenticated]

	def get_object(self, pk):
		print(f'104---------------{pk}')
		try:
			return Books.objects.get(pk=pk)
		except Books.DoesNotExist:
			raise Http404

	def get(self, request, pk):
		book_obj= self.get_object(pk)
		print(f'112---------------{book_obj}')
		serializer= BooksSerializer(book_obj)
		return Response (serializer.data)

	def put(self, request, pk):
		book_obj=self.get_object(pk)
		user_obj = get_object_or_404(User, email=request.user.email)
		if Books.book_add_by == user_obj:
			serializer=BookSerializer(book_obj, request.data)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data)
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		return Response ({ "error": "You have no authority to update this Store"})


	def delete(self, request, pk):
		book_obj=self.get_object(pk)
		user_obj = get_object_or_404(User, email=request.user.email)
		if Books.book_add_by == user_obj:
			book_obj.delete()
			return Response(status=status.HTTP_204_NO_CONTENT)
		return Response ({ "error": "You have no authority to delete this Store"})



