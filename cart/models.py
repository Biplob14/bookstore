from django.db import models

# Create your models here.


class DeliveryCharge(models.Model):
    delivery_charge = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(sellf):
        return "delivery cost"
