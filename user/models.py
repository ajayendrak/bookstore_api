from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
import re
from django.contrib.auth.models import UserManager
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.validators import RegexValidator
from twilio.rest import Client



# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):

	def validate_phone_number(value):
		if re.compile(r"\d{10}").match(value):
			return value
		else:
			raise ValidationError("Phone number entered is incorrect.")

	def validateEmail(email):
		if len(email) > 6:
			if re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', email) != None:
				return email
			else:
				raise ValidationError("Email entered is Incorrect.")
		raise ValidationError("Email is Incorrect")


	username = models.CharField(max_length=100)
	email=models.EmailField(validators=[validateEmail],blank=True, null=True, unique=True)
	first_name= models.CharField(max_length=100, blank=True, null=True)
	last_name= models.CharField(max_length=100, blank=True, null=True)
	start_date = models.DateTimeField(auto_now_add=True)
	is_staff = models.BooleanField(default=False)
	password= models.CharField(max_length=100)
	phone_number=models.CharField(validators=[validate_phone_number], max_length=10, blank=True, null=True, default='0000000000')

	def __str__(self):
		return self.username + " -- " + f"{self.id}"


	objects = UserManager()

	USERNAME_FIELD = "email"

	REQUIRED_FIELDS = ["username","first_name","last_name","password"]

	def get_tokens_for_user(self):
		refresh = RefreshToken.for_user(self)

		return {
			'refresh': str(refresh),
			'access': str(refresh.access_token),
		}


class OTP(models.Model):
	otp = models.CharField(max_length=4)
	phone = models.CharField(max_length=10)
	otp_count = models.IntegerField(default=0, help_text="Number of otp's sent.")
	otp_request_datetime = models.DateTimeField(auto_now=True)
	validated = models.BooleanField(default=False, help_text="If True, otp is validated.")


	def __str__(self):
		return f"OTP ({self.otp}) sent to phone {self.phone}"

	# Find your Account SID and Auth Token at twilio.com/console
	# and set the environment variables. See http://twil.io/secure

	def send_sms(self, otp, phone):
		if self.phone: 
			account_sid = 'ACe0ceab5839b7f97dc549fb924dab15c8'
			auth_token = '2a2caf68d1e5ffb5fdcab3977714fc8d'
			client = Client(account_sid, auth_token)

			message = client.messages \
			                .create(
			                     body=f"Hello! {self.otp} This is your OTP .",
			                     from_='+13185463757',
			                     to=f'+91{self.phone}'
			                 )

			print(message.sid)