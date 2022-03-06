
from django.db import models

# Create your models here.

class Park(models.Model):
    park_name = models.CharField(max_length=64)
    park_type = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)


class Order(models.Model):
    order_garage = models.ForeignKey(Park,on_delete=models.CASCADE, default=None)
    order_payment = models.CharField(max_length=50, null= True)

    class Meta():
        db_table = 'order_pay'
