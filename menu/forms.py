from django import forms
from .models import MenuItem

class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ['name', 'description', 'price']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'inp-control-1', 'placeholder': 'Name'}),
            'description': forms.TextInput(attrs={'class': 'inp-control-2' , 'placeholder': 'Description'}),
            'price': forms.NumberInput(attrs={'class': 'inp-control-3' , 'placeholder': 'Price'}),
        }