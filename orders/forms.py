from djnago import forms
from .models import Order
import razorpay

class OrderForm(forms.Form):
    amount = forms.IntegerField(min_value=100, required=False)

    def create_order(self):
        amount = self.amount
        client = razorpay.Client(auth=('apikey', 'apisecret'))

        order = Order.objects.create(amount=amount)

        client.set_app_details({"title" : "Django", "version" : "4.1.4"})

        data = { "amount": amount, "currency": "INR", "receipt": order.id }
        payment = client.order.create(data=data)
