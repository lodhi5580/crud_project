from django.contrib import admin
from .models import User, Product

@admin.register(User)
class Useradmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'password')

@admin.register(Product)
class Productadmin(admin.ModelAdmin):
    list_display = ('id', 'pname', 'description', 'price')