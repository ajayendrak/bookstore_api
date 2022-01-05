from django.shortcuts import render
from chat.models import Message
from user.models import User
# from django.http.response import Response
from rest_framework.permissions import IsAuthenticated
# from chat.serializers import MessageSerializer, UserSerializer
from user.serializers import UserSerializer
from rest_framework.views import APIView



# class GetUserAPIView(APIView):

# 	def get(self, request, pk):
		


def chat_menu(request):
    return render(request, 'chat/chat_menu.html')


