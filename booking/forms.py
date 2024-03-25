from django import forms
from django.forms.widgets import DateInput
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['table', 'date', 'time', 'num_guest']
        widgets = {
            'date': DateInput(attrs={'type': 'date'}),
        }