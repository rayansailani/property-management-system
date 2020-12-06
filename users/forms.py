from users.models import Account
from . models import Owners, Tenant, Buyers
from properties.models import PropertyForRent
from django import forms
from django.conf import settings
User = settings.AUTH_USER_MODEL


class RegisterOwners(forms.ModelForm):
    class Meta:
        model = Owners
        fields = [
            'acc_no',
        ]


class TenantRegistrationForm(forms.ModelForm):

    class Meta:
        model = Tenant
        fields = [
            'property_owner',
            'property',
            'aadhar_no',
            'acc_no',
            'address_proof',
            'ifsc_code',
        ]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.fields['property'].queryset = PropertyForRent.objects.all()
        accounts = Account.objects.filter(
            is_ppty_owner=True).exclude(id=self.user.id)
        self.fields['property_owner'].queryset = accounts


class BuyerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Buyers
        fields = ['catagory', ]
