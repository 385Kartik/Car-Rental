from django import forms
from .models import Car

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        # List the fields you want the user to fill out
        fields = [
            'brand', 
            'model', 
            'year', 
            'image', 
            'category', 
            'seating_capacity', 
            'fuel_type', 
            'transmission', 
            'location', 
            'price_per_day', 
            'description'
        ]
        # You can also add Bootstrap classes to the widgets here
        widgets = {
            'brand': forms.TextInput(attrs={'class': 'form-control'}),
            'model': forms.TextInput(attrs={'class': 'form-control'}),
            'year': forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'category': forms.TextInput(attrs={'class': 'form-control'}),
            'seating_capacity': forms.NumberInput(attrs={'class': 'form-control'}),
            'fuel_type': forms.TextInput(attrs={'class': 'form-control'}),
            'transmission': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'price_per_day': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }