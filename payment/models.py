from django.db import models

# Create your models here.



class BookOrder(models.Model):
	bookid=models.CharField(max_length=50)
	book = models.CharField(max_length=100)
	order_amount = models.CharField(max_length=25)
	order_payment_id = models.CharField(max_length=100)
	isPaid = models.BooleanField(default=False)
	order_date = models.DateTimeField(auto_now=True)


	def __str__(self):
		return self.order_product




