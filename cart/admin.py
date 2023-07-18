from django.contrib import admin

# Register your models here.
from .models import DeliveryCharge


@admin.register(DeliveryCharge)
class DeliveryChargeAdmin(admin.ModelAdmin):
    list_display = [
        'delivery_charge',
    ]

    def has_add_permission(self, *args, **kwargs):
        ''' handle data add permission '''
        return not DeliveryCharge.objects.exists()
