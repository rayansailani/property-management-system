from django import forms
from .models import PropertyForRent, PropertyForSale, Appointment, visit
from accounts.models import Account


class RentalRegistrationForm(forms.ModelForm):
    class Meta:
        model = PropertyForRent
        fields = [
            'property_name',
            'address',
            'floor_no',
            'no_rooms',
            'rent',
            'security_deposit',
            'image1',
            'image2',
            'image3',
            'image4',
            'description',
        ]


class PropertyRegistrationForm(forms.ModelForm):
    class Meta:
        model = PropertyForSale
        fields = [
            'no',
            'locality',
            'area',
            'city',
            'state',
            'width',
            'length',
            'cost_sqft',
            'ceritification',
            'description',
        ]


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = [
            'date_appointement',
            'time_appointment',
        ]


class RentAppointmentForm(forms.ModelForm):
    time_appointment = forms.TimeField(widget=forms.TimeInput(attrs={
        'class': 'form-control',
        'type': 'time',
    }))
    date_appointement = forms.DateField(widget=forms.DateInput(attrs={
        'class': 'form-control',
        'type': 'date',
    }))

    class Meta:
        model = visit
        fields = [
            'date_appointement',
            'time_appointment',
        ]
