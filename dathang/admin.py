from django.contrib import admin

from .models import Order,Order_Product,Voucher,diachigiaohang
# Register your models here.
admin.site.register(Order)
admin.site.register(Order_Product)
admin.site.register(Voucher)
admin.site.register(diachigiaohang)
