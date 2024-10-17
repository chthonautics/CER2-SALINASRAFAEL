from django.db import models

# Create your models here.
class users(models.Model):
    firstname = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    email = models.CharField(max_length=256)
    password_sha256 = models.CharField(max_length=64)

class products(models.Model):
    name = models.CharField(max_length=256)
    price = models.IntegerField()

class orders(models.Model):
    user_id = models.IntegerField()
    products = models.CharField(max_length=1024)
    status = models.BooleanField()
