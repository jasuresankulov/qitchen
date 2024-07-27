from django import forms
from .models import MenuItem, Reservation, Order

class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ['name', 'description', 'price']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'inp-control-1', 'placeholder': 'Name'}),
            'description': forms.TextInput(attrs={'class': 'inp-control-2' , 'placeholder': 'Description'}),
            'price': forms.NumberInput(attrs={'class': 'inp-control-3' , 'placeholder': 'Price'}),
        }
        
        

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


# class OrderForm(forms.ModelForm):
#     class Meta:
#         model = Order
#         fields = ('quantity',)


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_name', 'product_name', 'quantity', 'price']
