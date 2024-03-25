from django import forms
from django.forms.widgets import DateInput
from .models import Booking


class BookingForm(forms.ModelForm):
    
    class Meta:
        model = Booking
        fields = ['fname','lname','email','table', 'date', 'time', 'num_guest']
        widgets = {
            'date': DateInput(attrs={'type': 'date'}),
        }

        labels = {
            "fname": "First name:",
            "lname": "Last name",
            "email": "Email address",
            "num_guest": "How many guests? For more than 8 people, please contact us",
            "table": "Select your table, mind the capacity limit",
            "date": "Date",
            "time": "Time",
        }