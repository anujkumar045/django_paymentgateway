from django.shortcuts import render
import razorpay
from app.models import Order

# Create your views here.
def landing(req):
    return render(req,'landing.html')

# def pay_amount(req):
    if req.method=='POST':
        amount1=req.POST.get('amount')
        print(type(amount1))
        amount=float(amount1)*100
        client = razorpay.Client(auth =("rzp_test_pr99iascS1WRtU" , "UTDIzPGwICnAssu3Q3lk7zUi"))
        data = { "amount": amount, "currency": "INR", "receipt": "order_rcptid_11" }
        payment = client.order.create(data=data) 
        print(payment)
        Order.objects.create(
            order_id=payment.get('id'),
            amount=int(amount1)
        )
        return render(req,'landing.html',{'payment':payment,'amount':amount1})

def pay_amount(req):
    if req.method=='POST':
        amount1=req.POST.get('amount')
        print(type(amount1))
        amount=float(amount1)*100
        client = razorpay.Client(auth =("rzp_test_pr99iascS1WRtU" , "UTDIzPGwICnAssu3Q3lk7zUi"))
        data = { "amount": amount, "currency": "INR", "receipt": "order_rcptid_11" }
        payment = client.order.create(data=data)
        Order.objects.create(
            order_id=payment.get('id'),
            amount=int(amount1)
        )
        return render(req,'landing.html',{'payment':payment,'amount':amount1})
    
def payment_status(req):
    print(req.POST)
    order_id=req.POST.get('razorpay_order_id')
    razorpay_id=req.POST.get('razorpay_payment_id')   
    old_order=Order.objects.get(order_id=order_id)
    old_order.razorpay_id=razorpay_id
    old_order.payment_status=True
    old_order.save()
    return render(req,'success.html')    