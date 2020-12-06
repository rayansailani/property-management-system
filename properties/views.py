from django.shortcuts import render, redirect
from .forms import RentalRegistrationForm, PropertyRegistrationForm, AppointmentForm
from .models import PropertyForRent, PropertyForSale, Appointment
from .filters import PropertyFilter
# Create your views here.


def register_property_rent_view(request):
    context = {}
    if request.POST:
        form = RentalRegistrationForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.owner = request.user
            instance.save()
            return redirect('home')
    else:
        form = RentalRegistrationForm()
    context['ppty_reg_form'] = form
    return render(request, 'properties/register_ppty_rent.html', context)


def properties_view(request):
    properties = PropertyForRent.objects.filter(is_occupied=False)
    context = {
        'properties': properties,
    }
    return render(request, 'properties/property_list.html', context)


def property_detail_view(request, id):
    prop = PropertyForRent.objects.get(id=id)
    context = {
        'prop': prop,
    }
    return render(request, 'properties/property_detail.html', context)


def register_property_sale_view(request):
    context = {}
    if request.POST:
        form = PropertyRegistrationForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.owner = request.user
            instance.save()
            return redirect('dashboard')
    else:
        form = PropertyRegistrationForm()
    context['registration_form'] = form
    return render(request, 'properties/register_sale_ppty.html', context)


def properties_for_sale_view(request):
    properties = PropertyForSale.objects.all()
    myFilter = PropertyFilter(request.GET, queryset=properties)
    properties = myFilter.qs
    context = {
        "properties": properties,
        'myFilter': myFilter,
    }
    return render(request, "properties/properties_for_sale.html", context)


def appointment_view_form(request, id):
    context = {}
    property = PropertyForSale.objects.get(id=id)
    if request.POST:
        form = AppointmentForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.property = property
            instance.owner = property.owner
            instance.save()
            return redirect('dashboard')
    else:
        form = AppointmentForm()
    context['appointement_reg_form'] = form
    return render(request, 'properties/appointment.html', context)
