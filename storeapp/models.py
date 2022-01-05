from django.db import models
from user.models import User

# Create your models here.


class Store(models.Model):
	owner=models.ForeignKey(User, on_delete=models.CASCADE)
	storename = models.CharField(max_length=100)
	totalbooks=models.IntegerField(default=0)
	storeimage=models.ImageField(upload_to="images/")


	class Meta:
		db_table='store'



class Books(models.Model):
	book_add_by=models.ForeignKey(User, on_delete=models.CASCADE)
	from_store=models.ForeignKey(Store, on_delete=models.CASCADE)
	bookid=models.CharField(max_length=50, primary_key=True)
	bookname=models.CharField(max_length=100)
	bookprice=models.IntegerField(default=1)
	bookauthor=models.CharField(max_length=50)
	bookimage=models.ImageField(upload_to="images/")


	class Meta:
		db_table='books'


class DiscountBook(models.Model):
	book= models.OneToOneField(Books, on_delete=models.CASCADE)
	expiry_date= models.DateTimeField()
	