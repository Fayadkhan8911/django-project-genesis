from django import forms
from .models import item

class itemform(forms.ModelForm):
    class Meta:
        model = item
        fields = ['name', 'description', 'price', 'category', 'image']


        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter Item Name',
                'class': 'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent'
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Enter Item Description',
                'class': 'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent',
                'rows': 4
            }),
            'price': forms.NumberInput(attrs={
                'placeholder': 'Enter Item Price',
                'class': 'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent'
            }),
            'category': forms.Select(attrs={
                'class': 'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent'
            }),
        }   