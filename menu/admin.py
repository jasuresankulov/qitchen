from django.contrib import admin
from .models import MenuItem, Reservation

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'available','category')
    list_filter = ('available',)
    search_fields = ('name', 'description')



class ReservationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'number_of_guests', 'reservation_date', 'reservation_time')
    search_fields = ('name', 'email')
    list_filter = ('reservation_date', 'reservation_time')

admin.site.register(Reservation, ReservationAdmin)

