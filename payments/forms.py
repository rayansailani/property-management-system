from django import forms
from .models import RentPayment
from users.models import Owners


class PaymentRentForm(forms.ModelForm):
    class Meta:
        model = RentPayment
        fields = ()
