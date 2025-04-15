
from django import forms
from .models import instock

class ReceiveStockForm(forms.Form):
    flavor = forms.ModelChoiceField(
        queryset=instock.objects.all(), 
        label="Select Flavor",
        empty_label="Choose a Flavor",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    quantity = forms.IntegerField(
        min_value=1, 
        label="Quantity", 
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )