from django.urls import path
from .views import *


urlpatterns=[
	path("register", Register.as_view(), name='register'),
	path("create_otp", CreateOTP.as_view(), name='create_otp'),
	path("login", Login.as_view(), name='login'),
]