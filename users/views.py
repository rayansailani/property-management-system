from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from accounts.models import Account
from . forms import RegisterOwners, TenantRegistrationForm, BuyerRegistrationForm
from properties.models import PropertyForRent, PropertyForSale, Appointment
from django.shortcuts import render, redirect
from . models import Tenant
import datetime
from payments.models import RentPayment
from django.conf import settings
User = settings.AUTH_USER_MODEL


def register_owner_view(request):
    account = Account.objects.get(id=request.user.id)
    if request.method == "POST":
        form = RegisterOwners(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.owner = request.user
            account.is_ppty_owner = True
            account.save()
            instance.save()
            return redirect('home')
    else:
        form = RegisterOwners()
    return render(request, 'users/register_user.html', {'register_owner_form': form})


def register_tenant_view(request):
    account = Account.objects.get(id=request.user.id)
    properties = PropertyForRent.objects.all()
    if request.POST:
        form = TenantRegistrationForm(request.POST, user=request.user)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.tenant = request.user
            account.is_tenant = True
            pid = instance.property.id
            property = properties.get(id=pid)
            property.is_occupied = True
            property.save()
            account.save()
            instance.save()
            return redirect('home')
    else:
        form = TenantRegistrationForm(user=request.user)
    return render(request, 'users/register_tenant.html', {'tenant_reg_form': form, })


def tenant_detail_view(request, tenant_id):
    tenant = Tenant.objects.get(id=tenant_id)
    context = {
        'tenant': tenant,
    }
    return render(request, 'users/tenant_detail.html', context)


def remove_tenant_view(request, tenant_id):
    item = Tenant.objects.get(id=tenant_id)
    user = Account.objects.get(id=item.tenant.id)
    ppty = PropertyForRent.objects.get(id=item.property.id)
    if request.POST:
        user.is_tenant = False
        ppty.is_occupied = False
        ppty.save()
        user.save()
        item.delete()
        return redirect('dashboard')
    context = {
        "item": item,
    }
    return render(request, 'users/remove_tenant.html', context)


def load_cities(request):
    owner_id = request.GET.get('owner_id')
    properties = PropertyForRent.objects.filter(owner_id=owner_id)
    properties = properties.filter(is_occupied=False)
    return render(request, 'users/property_dropdown_list_options.html', {'properties': properties})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)


@login_required(login_url="/accounts/login/")
def dashboard_view(request):
    context = {}
    tenants = Tenant.objects.filter(property_owner=request.user)
    rents = {
    }
    try:
        rental_house = Tenant.objects.get(tenant=request.user)
        payment_status = RentPayment.objects.filter(
            month_of=datetime.date.today().month)
        print(payment_status)
        payment_status = payment_status.get(sender=request.user)
        if payment_status.rent_paid == True:
            context['rent_status'] = True
    except Tenant.DoesNotExist:
        rental_house = None
        # context['rent_status'] = False
    except RentPayment.DoesNotExist:
        context['rent_status'] = False
    properties = PropertyForRent.objects.filter(owner=request.user)

    unoccupied_houses = properties.filter(is_occupied=False)
    appointments = Appointment.objects.filter(owner=request.user)
    context['appointments'] = appointments
    rents_done = 0
    rents_left = 0
    occupied_houses = PropertyForRent.objects.filter(
        owner=request.user).filter(is_occupied=True)
    rents_current_owner = RentPayment.objects.filter(
        reciever=request.user).filter(month_of=datetime.date.today().month)
    rents_done = rents_current_owner.count()
    rents_left = occupied_houses.count() - rents_done
    context['rents_done'] = rents_done
    context['rents_left'] = rents_left
    context['rents'] = rents_current_owner
    no_properties_total = properties.count()
    no_properties_occupied = occupied_houses.count()
    no_properties_unoccupied = unoccupied_houses.count()
    total_rent = 0
    total_deposit = 0
    average_rent = 0
    for x in occupied_houses:
        total_rent += x.rent
        total_deposit += x.security_deposit
    try:
        average_rent = total_rent/no_properties_occupied
    except:
        average_rent = 0
    context['average_rent'] = average_rent
    context['total_deposit'] = total_deposit
    context['no_properties_unoccupied'] = no_properties_unoccupied
    context['no_properties_occupied'] = no_properties_occupied
    context['total_properties_rent'] = no_properties_total
    context['rental_house'] = rental_house
    context['tenants'] = tenants
    context['unoccupied_houses'] = unoccupied_houses
    context['total_rent'] = total_rent
    sale_houses = PropertyForSale.objects.filter(owner=request.user)
    context['houses'] = sale_houses
    return render(request, 'users/dashboard.html', context)


def buyer_registration_view(request):
    context = {

    }
    if request.POST:
        form = BuyerRegistrationForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.name = request.user
            instance.save()
            return redirect('dashboard')
    else:
        form = BuyerRegistrationForm()
    context['buyer_registration_form'] = form
    return render(request, 'users/register_buyer.html', context)
