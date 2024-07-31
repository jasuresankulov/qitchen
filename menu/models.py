from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError


class MenuItem(models.Model):
    CHOICE_CATEGORY = [
        ('Hammasi','Hammasi'),
        ("Go'shtli","Go'shtli"),
        ('Salatlar','Salatlar'),
        ('Shirinlik','Shirinlik'),
        ('Ichimliklar','Ichimliklar')
    ]
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    available = models.BooleanField(default=True)
    category = models.CharField(max_length=15, choices=CHOICE_CATEGORY, default='Hammasi')
    image = models.ImageField(upload_to='images/', default='images/default.jpg')
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

    class Meta:
        unique_together = ('name', 'reservation_date', 'reservation_time')

    def __str__(self):
        return f'Reservation for {self.name} on {self.reservation_date} at {self.reservation_time}'
    
    def clean(self):
        if Reservation.objects.filter(
                name=self.name,
                reservation_date=self.reservation_date,
                reservation_time=self.reservation_time
        ).exclude(id=self.id).exists():
            raise ValidationError('A reservation with the same name, date, and time already exists.')

    def save(self, *args, **kwargs):
        self.clean()
        super(Reservation, self).save(*args, **kwargs)


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
    author_of_order = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f'Order {self.id} by {self.customer_name}'


