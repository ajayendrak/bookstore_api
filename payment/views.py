from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import OrderSerializer
import environ
import razorpay
from rest_framework.response import Response


env = environ.Env()
environ.Env.read_env()


class StartPayment(APIView):
	permission_classes = [IsAuthenticated]

	def post(self, request):
		amount = request.data['amount']
		book = request.data['book']
		bookid = request.data['bookid']


		client = razorpay.Client(auth=(env('PUBLIC_KEY'), env('SECRET_KEY')))

		# create razorpay order
		payment = client.order.create({"amount": int(amount) * 100, 
							   "currency": "INR", 
							   "payment_capture": "1"})

		# we are saving an order with isPaid=False
		order = BookOrder.objects.create(book=book, 
									 order_amount=amount,
									 bookid=bookid,
									 order_payment_id=payment['id'])

		serializer = OrderSerializer(order)


		"""order response will be 
		{'id': 17, 
		'order_date': '20 November 2020 03:28 PM', 
		'order_product': '**product name from frontend**', 
		'order_amount': '**product amount from frontend**', 
		'order_payment_id': 'order_G3NhfSWWh5UfjQ', # it will be unique everytime
		'isPaid': False}"""

		data = {
			"payment": payment,
			"order": serializer.data
		}
		return Response(data)


class HandlePaymentSuccess(APIView):
	permission_classes = [IsAuthenticated]


	def post(self, request):
		user = request.user
		# res = json.loads(request.data["Response"])
		res = request.data
		"""res will be:
		{'razorpay_payment_id': 'pay_G3NivgSZLx7I9e', 
		'razorpay_order_id': 'order_G3NhfSWWh5UfjQ', 
		'razorpay_signature': '76b2accbefde6cd2392b5fbf098ebcbd4cb4ef8b78d62aa5cce553b2014993c0'}
		"""

		ord_id = ""
		raz_pay_id = ""
		raz_signature = ""


		# res.keys() will give us list of keys in res
		for key in res.keys():
			if key == 'order_id':
				ord_id = res[key]
			elif key == 'payment_id':
				raz_pay_id = res[key]
			elif key == 'razorpay_signature':
				raz_signature = res[key]


		# get order by payment_id which we've created earlier with isPaid=False
		order_obj = BookOrder.objects.get(order_id=ord_id)
		if raz_pay_id:
			pass
		else:
			print("Redirect to error url or error page")
			return Response({'error': 'Something went wrong'})
		order_objorder_obj.payment_id= raz_pay_id

		data = {
			'razorpay_order_id': ord_id,
			'razorpay_payment_id': raz_pay_id,
			'razorpay_signature': raz_signature
		}

		client = razorpay.Client(auth=(env('PUBLIC_KEY'), env('SECRET_KEY')))
		# client = razorpay.Client(auth=('rzp_test_i6F2nCkFfuD0xF', 'wHce7MeW1iM5oxWlwLxrpOX6'))


		# checking if the transaction is valid or not if it is "valid" then check will return None
		# check = client.utility.verify_payment_signature(data)


		# if check is not None:
		# 	print("Redirect to error url or error page")
		# 	return Response({'error': 'Something went wrong'})

		# if payment is successful that means check is None then we will turn isPaid=True
		order_obj.is_paid = True
		order_obj.save()
		res_data = {
			'message': 'payment successfully received!'
		}

		
		
		# if payment_status_obj.subscription_type.subscription_type == "premium":
		# 	try:
		# 		premium_subscription = PremiumSubscription.objects.get(user = user)
		# 		if premium_subscription.end_date:
		# 			if premium_subscription.end_date.date() < datetime.now().date():
		# 				premium_subscription.end_date = datetime.now()+timedelta(days=30)
		# 			else:
		# 				premium_subscription.end_date = premium_subscription.end_date + timedelta(days=30)
		# 	except Exception as e:
		# 		premium_subscription = PremiumSubscription.objects.create(user = user)
		# 		premium_subscription.end_date = datetime.now()+timedelta(days=30)
		# 	premium_subscription.premium_amount = payment_status_obj.total_amount_of_product
		# 	premium_subscription.save()
		# if payment_status_obj.subscription_type.subscription_type == "livein":
		# 	try:
		# 		livein_subscription = LiveInSubscription.objects.get(user = user)
		# 		if livein_subscription.end_date:
		# 			if livein_subscription.end_date.date() < datetime.now().date():
		# 				livein_subscription.end_date = datetime.now() + timedelta(days=30)
		# 			else:
		# 				livein_subscription.end_date = livein_subscription.end_date + timedelta(days=30)
		# 	except Exception as e:
		# 		livein_subscription = LiveInSubscription.objects.create(user = user)
		# 		livein_subscription.end_date = datetime.now()+timedelta(days=30)
		# 	livein_subscription.live_in_me_amount = payment_status_obj.total_amount_of_product
		# 	livein_subscription.save()
		return Response(res_data)