from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.response import Response
from django.contrib.auth import authenticate, logout, login
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
import random, pytz



class Register(APIView):
	permission_classes = []
	serializer_class = None


	def post(self, request):
		username= request.data.get("username")
		email= request.data.get("email")
		first_name = request.data.get("first_name")
		last_name = request.data.get("last_name")
		phone_number = request.data.get("phone_number")
		password1= request.data.get("password1")
		password2= request.data.get("password2")


		if username and email and first_name and last_name and password1 and password2:
			user_obj=User.objects.filter(email=email)
			if user_obj.exists():
				return Response(
					{
						"status": "Error",
						"message": "User with the given email already exists.",
					},
					status=status.HTTP_422_UNPROCESSABLE_ENTITY,
				)

			else:
				data = {
							"username" : username,
							"email" : email,
							"first_name" : first_name,
							"last_name" : last_name,
							
						}
				if password1 == password2:
					user=User.objects.create(username=username, email=email, first_name=first_name, last_name=last_name, password=password1)
					user.save()
					return Response(
								{
									"user": data
								},
								status=status.HTTP_201_CREATED,
							)

				else:
					return Response(
						{
							"status": "Error",
							"message": "Password does not matching.",
						},
						status=status.HTTP_417_EXPECTATION_FAILED,
					)


		else:
			return Response(
				{
					"status": "Error",
					"message": "Please provide all the required data to register.",
				},
				status=status.HTTP_417_EXPECTATION_FAILED,
			)

class Login(APIView):
	permission_classes=[]
	serializer_class=None

	def post(self, request, *args, **kwargs):
		email= request.data.get("email")
		password=request.data.get("password")
		print(f'78--------------{email}-----{password}')


		if email and password:
			# user=authenticate(request,email=email, password=password)
			# print(f'82----------------{user}')
			# login(request, user)
			user_obj = User.objects.filter(email=email)
			res = user_obj[0].get_tokens_for_user()
			
			return Response(
				{
					"login": "Successful",
					"email": email ,
					"token": res['access']
				},
				status=status.HTTP_201_CREATED,
			)


		else:
			return Response(
				{
					"status": "Error",
					"message": "Email number does not entered. Enter phone number first to continue.",
				},
				status=status.HTTP_417_EXPECTATION_FAILED,
			)


class Logout(APIView):
	permission_classes=[]
	serializer_class=None

	def post(self, request, *args, **kwargs):
		email= request.data.get("email")
		password=request.data.get("password")


class CreateOTP(APIView):
	permission_classes=[]
	serializer_class=None

	def post(self, request, *args, **kwargs):
		phone_number = request.data.get("phone_number")
		if len(phone_number)== 10:
			otp = str(random.randint(1000, 9999))
			otp_obj = OTP(otp=otp, phone=phone_number)
			otp_obj.save()
			otp_obj.send_sms(otp, phone_number)
			serializer=OTPSerializer(otp_obj)
			return Response(serializer.data, status=status.HTTP_200_OK)



		
