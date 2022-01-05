from rest_framework import serializers
from .models import *
from rest_framework.serializers import SerializerMethodField



class OrderSerializer(serializers.ModelSerializer):

	class Meta:
		model = BookOrder
		fields = "__all__"