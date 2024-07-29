from rest_framework import serializers
from .models import MenuItem, Reservation,Order

# from .models import Book, BookImage

class MenuItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['url','name', 'description', 'price', 'available','category']

# ====================================================================================

class ReservationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Reservation
        fields = ['url', 'name', 'email', 'phone_number', 'number_of_guests', 'reservation_date', 'reservation_date', 'reservation_time', 'special_requests']
        
        

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

