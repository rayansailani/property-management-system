from django.shortcuts import render
from users.models import Owners
from django.db import connection
from accounts.models import Account
from properties.models import PropertyForRent, PropertyForSale
from payments.models import RentPayment


def homepage_view(request):
    # curse = connection.cursor()
    # accounts = curse.execute('select * from accounts_account')
    accounts = Account.objects.all().count()
    properties_for_rent = PropertyForRent.objects.all().count()
    properties_for_sale = PropertyForSale.objects.all().count()
    total_amt = 0
    rents = RentPayment.objects.all()
    for x in rents:
        total_amt += x.rent_amount
    context = {
        "accounts": accounts,
        'properties_for_rent': properties_for_rent,
        'properties_for_sale': properties_for_sale,
        'total_amt': total_amt,
    }
    return render(request, 'home.html', context)
