from logging import PlaceHolder
from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['item_name', 'item_desc', 'item_price', 'item_image']

        labels = {
            'item_name': '',
            'item_desc': '',
            'item_price': '',
            'item_image': ''
        }

        widgets = {
            'item_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Name of the Item"}),
            'item_desc': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Description"}),
            'item_price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Price"}),
            'item_image': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Image URL"})
        }
