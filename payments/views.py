from django.shortcuts import render, redirect
from .forms import PaymentRentForm
from users.models import Tenant, Owners
from properties.models import PropertyForRent
from .models import RentPayment
import datetime
import secrets
# Create your views here.


def payment_view(request):
    context = {}
    token = secrets.token_hex(16)
    current_tenant = Tenant.objects.get(tenant=request.user)
    print(current_tenant.property_owner)
    current_owner = Owners.objects.get(
        owner=current_tenant.property_owner)
    print(current_owner)
    property = PropertyForRent.objects.filter(owner=current_owner.owner)
    print(property)
    p_id = current_tenant.property.id
    property = property.get(id=p_id)
    print(property)
    # instance = form.save(commit=False)
    sender = request.user
    sender_account_no = current_tenant.acc_no
    reciever = current_owner.owner
    rev_account_no = current_owner.acc_no
    ifsc_code = current_tenant.ifsc_code
    rent_amount = property.rent
    rent_paid = True

    if request.POST:
        # form = PaymentRentForm(request.POST)
        # if form.valid():
        RentPayment.objects.create(
            sender=sender,
            transaction_id=token,
            sender_account_no=sender_account_no,
            reciever=reciever,
            rev_account_no=rev_account_no,
            ifsc_code=ifsc_code,
            property=property,
            rent_amount=rent_amount,
            rent_paid=rent_paid,
            month_of=datetime.date.today().month,
        )

        return redirect('dashboard')
    form = PaymentRentForm()
    context['rent_payment_form'] = form
    context['rent'] = property.rent
    return render(request, 'payments/payment.html', context)
