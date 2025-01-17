from django import forms
from .models import MenuItem, Reservation, Order

class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ['name', 'description', 'price', 'category', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'inp-control-1', 'placeholder': 'Ismingiz'}),
            'description': forms.TextInput(attrs={'class': 'inp-control-2', 'placeholder': 'Malumot'}),
            'price': forms.NumberInput(attrs={'class': 'inp-control-3', 'placeholder': 'Narxi'}),
            'category': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Kategoriyalar'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'})
        }
        
        

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['name', 'email', 'phone_number', 'number_of_guests', 'reservation_date', 'reservation_time']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ismingiz'}),
            'email': forms.EmailInput(attrs={'class': 'form-control' , 'placeholder': 'Emailingiz'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control-1' , 'placeholder': 'Telefon Raqamingiz'}),
            'number_of_guests': forms.NumberInput(attrs={'class': 'form-control-2', 'placeholder':'Mexmonlar Soni'}),
            'reservation_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control-2', 'placeholder': 'Sana'}),
            'reservation_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control-2', 'placeholder':'Vaqt   '}),
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
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['customer_name'].widget.attrs.update({'placeholder': 'Mijoz nomi'})
        self.fields['product_name'].widget.attrs.update({'placeholder': 'Mahsulot nomi'})
        self.fields['quantity'].widget.attrs.update({'placeholder': 'Miqdori'})
        self.fields['price'].widget.attrs.update({'placeholder': 'Narxi'})


