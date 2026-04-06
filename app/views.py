from django.shortcuts import render
import razorpay
from app.models import Order

# Create your views here.
def landing(req):
    return render(req,'landing.html')

def pay_amount(req):
    if req.method=='POST':
        amount1=req.POST.get('amount')
        print(type(amount1))
        amount=float(amount1)*100
        client = razorpay.Client(auth =("rzp_test_pr99iascS1WRtU" , "UTDIzPGwICnAssu3Q3lk7zUi"))
        data = { "amount": 50000, "currency": "INR", "receipt": "order_rcptid_11" }
        payment = client.order.create(data=data) 
        print(payment)
        Order.objects.create(
            order_id=payment.get('id'),
            amount=int(amount1)
        )
        return render(req,'landing.html',{'payment':payment,'amount':amount1})