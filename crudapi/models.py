from django.db import models

class User(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)


class Product(models.Model):
    pname = models.CharField(max_length=225)
    description = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)