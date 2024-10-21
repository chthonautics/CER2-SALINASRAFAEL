from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(user)
admin.site.register(product)
admin.site.register(order)
admin.site.register(recycle)
admin.site.register(orderproduct)