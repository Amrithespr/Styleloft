from django.contrib import admin

from cart.models import OrderStatus, Delivary
from shopowner.models import Referal

# Register your models here.

admin.site.register(OrderStatus)
admin.site.register(Referal)
admin.site.register(Delivary)

