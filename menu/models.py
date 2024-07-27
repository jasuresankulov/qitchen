from django.db import models
from django.contrib.auth.models import User


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Reservation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    number_of_guests = models.IntegerField()
    reservation_date = models.DateField()
    reservation_time = models.TimeField()
    special_requests = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Reservation for {self.name} on {self.reservation_date} at {self.reservation_time}'


# class Order(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     menuItem = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField()
#     total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
#     order_date = models.DateField(auto_now_add=True)
#     order_time = models.TimeField(auto_now_add=True)
    
#     def save(self, *args, **kwargs):
#         self.total_price = self.menuItem.price * self.quantity
#         super().save(*args, **kwargs)    

from django.db import models

class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order {self.id} by {self.customer_name}'
