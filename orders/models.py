from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class Order(models.Model):
    rz_order_id = models.CharField(_("Razorpay Order ID"), max_length=100)
    amount = models.PositiveIntegerField(_("Amount"))
    payment_success = models.BooleanField(_("Payment Status"))
    payment_id = models.CharField(_("Payment ID"), max_length=100)

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Order_detail", kwargs={"pk": self.pk})
