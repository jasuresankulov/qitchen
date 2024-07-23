from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['name', 'email', 'phone_number', 'number_of_guests', 'reservation_date', 'reservation_time']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control' , 'placeholder': 'Email'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control-1' , 'placeholder': 'Phone number'}),
            'number_of_guests': forms.NumberInput(attrs={'class': 'form-control-2', 'placeholder':'Guests'}),
            'reservation_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control-2', 'placeholder': 'Date'}),
            'reservation_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control-2', 'placeholder':'Time   '}),
            'special_requests': forms.Textarea(attrs={'class': 'form-control'}),
        }


