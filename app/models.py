from django.db import models

# Create your models here.
class Order(models.Model):
    order_id=models.CharField(max_length=30)
    amount=models.IntegerField()
    razorpay_id=models.CharField(max_length=30)
    payment_status=models.BooleanField(default=False)
