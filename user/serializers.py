from rest_framework import serializers
from .models import *

class OTPSerializer(serializers.ModelSerializer):

	class Meta:
		model= OTP
		fields= "__all__"



class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'password']