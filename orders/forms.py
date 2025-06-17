from django import forms
from .models import Order

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'customer_name', 'customer_phone', 'customer_email', 'customer_address',
            'pickup_address', 'delivery_address', 'pickup_date', 'delivery_date'
        ]
        widgets = {
            'customer_name': forms.TextInput(attrs={'class': 'form-control'}),
            'customer_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'customer_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'customer_address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'pickup_address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'delivery_address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'pickup_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'delivery_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make pickup and delivery addresses optional
        self.fields['pickup_address'].required = False
        self.fields['delivery_address'].required = False
        self.fields['pickup_date'].required = False
        self.fields['delivery_date'].required = False 