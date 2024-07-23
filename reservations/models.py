from django.db import models

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
