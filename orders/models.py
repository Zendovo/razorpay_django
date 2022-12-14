from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class Order(models.Model):
    order_id = models.CharField(_("Order ID"), max_length=50)    

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Order_detail", kwargs={"pk": self.pk})
)