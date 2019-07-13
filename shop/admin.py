from django.contrib import admin
from shop.models import *

# Register your models here.
admin.site.register(customer)
admin.site.register(Book)
admin.site.register(order)
admin.site.register(Cart)
admin.site.register(cartitems)
admin.site.register(orderdetail)