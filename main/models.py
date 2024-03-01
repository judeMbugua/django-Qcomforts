from django.db import models
from django.contrib.auth.models import User
from django.core.validators import ValidationError
import datetime



item_categories = (
    ("shirt", "Shirt"),
    ("hoodie", "Hoodie"),
)


item_sizes = (
    ("small", "Small"),
    ("medium", "Medium"),
    ("large", "Large"),
    ("extra-large", "Extra-large"),
)


item_colors = (
    ("white", "White"),
    ("black", "Black"),
    ("green", "Green"),
    ("red", "Red"),
    ("blue", "Blue"),
    ("yellow", "Yellow"),
    ("orange", "Orange"),
    ("brown", "Brown"),
)

item_offer = (
    ("yes", "Yes"),
    ("no", "No"),
)


statuses = (
    ("Pending", "Pending"),
    ("Out For Shipping", "Out For Shipping"),
    ("Completed", "Completed"),
)


class Clothe(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE, related_name="clothe")
    category = models.CharField(max_length=8, choices=item_categories)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="itemsImages")
    price = models.CharField(max_length=10)
    desc = models.CharField(max_length=200)
    color = models.CharField(max_length=8, choices=item_colors)
    size = models.CharField(max_length=15, choices=item_sizes)
    stockCount = models.CharField(max_length=5)
    offer = models.CharField(max_length=8, choices=item_offer, default="No")
    old_price = models.CharField(max_length=10, default=0)

    #shows category of objects in django admin dashboard
    def __str__(self):
        return self.category


# Customer Orders
class Order(models.Model):
    product = models.ForeignKey(Clothe, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    size = models.CharField(max_length=15)
    address = models.CharField(max_length=100,null=True)
    phone = models.CharField(max_length=20, default="")
    order_id = models.CharField(max_length=20,null=True)
    status = models.CharField(max_length=150,choices=statuses,default="Pending")
    tracking_no = models.CharField(max_length=20,null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    
    def __str__(self):
        return "{} - {} - {} - {}".format(self.id,self.product.name,self.customer.username,self.tracking_no)


class OrderItem(models.Model):
    _order = models.ForeignKey(Order,on_delete=models.CASCADE)
    product = models.ForeignKey(Clothe,on_delete=models.CASCADE)
    price = models.CharField(max_length=50,null=False)
    quantity = models.IntegerField(null=False)
    
    
    
    def __str__(self):
        return "{} - {}".format(self._order.id,self._order.tracking_no)