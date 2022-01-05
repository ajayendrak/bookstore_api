from django.contrib import admin
from .models import *



class UserAdmin(admin.ModelAdmin):
    fields = ['id', 'username', 'email', 'first_name', 'last_name', 'start_date', 'is_staff', 'password', 'phone_number']
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'is_staff')
    list_per_page = 25
admin.site.register(User, UserAdmin)

admin.site.register(OTP)