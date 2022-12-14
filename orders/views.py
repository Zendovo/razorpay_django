from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.views import View
from .models import Order
from .forms import OrderForm

import hmac
import hashlib

# Create your views here.
class OrderFormView(FormView):
    template_name = "orders/order.html"
    form_class = OrderForm

    def form_valid(self, form):
        form.create_order()
        return super().form_valid(form)


class PaymentView(View):
    def get(self, request, *args, **kwargs):
        order_id = self.kwargs['id']

        order = Order.objects.get(id=order_id)
        return render(request, 'orders/payment.html', { 'order_id': order.rz_order_id, 'payment_id': order.payment_id, 'amount': order.amount })


class SuccessView(View):
    def post(self, request):
        order_id = request.POST['order_id']
        payment_id = request.POST['payment_id']
        signature = request.POST['signature']

        order = Order.objects.get(rz_order_id=order_id)

        message = order_id + '|' + payment_id
        generated_signature = hmac.new(bytes('API_SECRET' , 'utf-8'), msg = bytes(message , 'latin-1'), digestmod = hashlib.sha256).hexdigest().upper()

        order.payment_id = payment_id
        order.payment_status = True
        order.save()

        if signature == generated_signature:
            return render(request, 'orders/success.html')
        else:
            return redirect(f'/{order.id}')