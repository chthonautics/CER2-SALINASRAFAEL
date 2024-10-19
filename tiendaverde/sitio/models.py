from django.db import models

# Create your models here.
class users(models.Model):
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=256)
    password_sha256 = models.CharField(max_length=64)

class products(models.Model):
    name = models.CharField(max_length=256)
    price = models.IntegerField()

class orders(models.Model):
    user_id = models.IntegerField()
    status = models.BooleanField()
    
# used because it's a many:many relationship
class orderproducts(models.Model):
    product_id = models.IntegerField()
    order_id = models.IntegerField()
