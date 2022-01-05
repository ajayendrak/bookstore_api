from rest_framework import serializers
from .models import Store, Books
from rest_framework.serializers import SerializerMethodField


class StoreSerializer(serializers.ModelSerializer):



	class Meta:
		model = Store
		fields = [
			"id",
			"owner",
			"storename",
			"storeimage"
		]



class BooksSerializer(serializers.ModelSerializer):
	class Meta:
		model = Books
		fields= "__all__"