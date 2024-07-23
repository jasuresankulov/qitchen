from rest_framework import serializers
from .models import Reservation

class ReservationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Reservation
        fields = ['url', 'name', 'email', 'phone_number', 'number_of_guests', 'reservation_date', 'reservation_date', 'reservation_time', 'special_requests']
        
        

