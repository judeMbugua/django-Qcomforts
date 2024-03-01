from django.contrib import admin
from .models import Clothe,Order,OrderItem

# Register your models here.
admin.site.register(Clothe)
admin.site.register(Order)
admin.site.register(OrderItem)