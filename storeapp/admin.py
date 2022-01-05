from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Store),
admin.site.register(Books),
admin.site.register(DiscountBook),



# class BookAdmin()