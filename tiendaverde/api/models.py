from django.db import models

# Create your models here.
class user(models.Model):
    name = models.CharField(max_length=128)
    email = models.CharField(max_length=128, unique=True)
    password_sha256 = models.CharField(max_length=64)
    session_token = models.CharField(max_length=32)

class product(models.Model):
    name = models.CharField(max_length=128)
    price = models.IntegerField()

class order(models.Model):
    user = models.ForeignKey("user", on_delete=models.CASCADE)
    status = models.BooleanField()
    
# used because it's a many:many relationship
class orderproduct(models.Model):
    product_id = models.ForeignKey("product", on_delete=models.CASCADE)
    order_id = models.ForeignKey("order", on_delete=models.CASCADE)

class recycle(models.Model):
    name = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    address = models.CharField(max_length=256)
    comment = models.CharField(max_length=1024)