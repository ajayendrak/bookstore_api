from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt



urlpatterns=[
	path('menu', views.chat_menu, name='chat-menu')
] 
