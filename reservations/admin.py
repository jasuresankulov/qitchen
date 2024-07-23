from django.contrib import admin
from .models import Reservation

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'number_of_guests', 'reservation_date', 'reservation_time')
    search_fields = ('name', 'email')
    list_filter = ('reservation_date', 'reservation_time')

admin.site.register(Reservation, ReservationAdmin)
